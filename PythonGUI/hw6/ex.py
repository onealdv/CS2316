import pymysql
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QDialog,
    QGroupBox,
    QVBoxLayout,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QLabel,
    qApp,
    QAction,
    QSplitter,
    QListView,
    QTableWidget,
    QTableWidgetItem
)

class TableDialog(QDialog):
    def __init__(self, column_headers, rows):
        super(TableDialog, self).__init__()
        self.setModal(True)
        self.setWindowTitle("")

        table = QTableWidget(len(rows), len(rows[0]), self)
        table.setHorizontalHeaderLabels(column_headers)
        for i, row in enumerate(rows):
            for j, field in enumerate(row):
                item = QTableWidgetItem(field)
                table.setItem(i, j, item)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(table)
        vbox_layout.addWidget(buttons)
        self.setLayout(vbox_layout)


class MainWindow(QWidget):

    def __init__(self, db):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MySQL Browser")
        cursor = connection.cursor()
        cursor.execute("show tables")
        vbox_layout = QVBoxLayout()
        for row in cursor:
            table = row[f"Tables_in_{db}"]
            vbox_layout.addWidget(self.make_button(db, table))
        self.setLayout(vbox_layout)

    def make_button(self, db, table):
        button = QPushButton(table, self)
        button.clicked.connect(lambda: self.display(db, table))
        return button

    def display(self, db, table):
        curs = connection.cursor()
        query = f"select * from {table}"
        curs.execute(query)
        rows = []
        first_row = curs.fetchone()
        column_headers = [str(k).strip() for k, v in first_row.items()]
        rows.append([str(v).strip() for k, v in first_row.items()])
        for row in curs:
            rows.append([str(v).strip() for k, v in row.items()])

        dlg = TableDialog(column_headers, rows)
        dlg.exec()


class DbLoginDialog(QDialog):
    def __init__(self):
        super(DbLoginDialog, self).__init__()
        self.setModal(True)
        self.setWindowTitle("Login to MySQL Server")

        self.host = QLineEdit("localhost")
        self.user = QLineEdit("root")
        self.password = QLineEdit()
        self.db = QLineEdit()

        form_group_box = QGroupBox("MySQL Server Login Credentials")
        layout = QFormLayout()
        layout.addRow(QLabel("Host:"), self.host)
        layout.addRow(QLabel("User:"), self.user)
        layout.addRow(QLabel("Password:"), self.password)
        layout.addRow(QLabel("Database:"), self.db)
        form_group_box.setLayout(layout)

        # Consider these 3 lines boiler plate for a standard Ok | Cancel dialog
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(form_group_box)
        vbox_layout.addWidget(buttons)
        self.setLayout(vbox_layout)
        self.password.setFocus()

if __name__=='__main__':
    app = QApplication(sys.argv)


    login = DbLoginDialog()

    # This is how you check which button the user used to dismiss the dialog.
    if login.exec() == QDialog.Accepted:
        # connection is global so we can use it in any class, function, or method
        # defined in this module
        global connection
        try:
            connection = pymysql.connect(host=login.host.text(),
                                         user=login.user.text(),
                                         password=login.password.text(),
                                         db=login.db.text(),
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            print(f"Couldn't log {login.user.text()} in to MySQL server on {login.host.text()}")
            print(e)
            qApp.quit()
            sys.exit()
        main = MainWindow(login.db.text())
        main.show()
        sys.exit(app.exec_())
    else:
        qApp.quit()
