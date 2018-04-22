import pymysql
import sys
from PyQt5.QtWidgets import (
   QApplication,
    QMainWindow,
    qApp,
    QAction,
    QWidget,
    QLabel,
    QLineEdit,
    QSplitter,
    QPushButton,
    QComboBox,
    QTableView,
    QRadioButton,
    QTableWidget,
    QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,
    QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QVariant
)
#    QLineEdit te
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Marta Database")

        routesbtn = QPushButton("Routes")
        stopsbtn = QPushButton("Stops")
        vehiclesbtn = QPushButton("Vehicles")
        passengerbtn = QPushButton("Passenger by Date")
        datelabel = QLabel("Date")
        self.datetext = QLineEdit()

        grid = QGridLayout()
        grid.addWidget(routesbtn,1,0,1,3)
        grid.addWidget(stopsbtn,2,0,1,3)
        grid.addWidget(vehiclesbtn,3,0,1,3)
        grid.addWidget(passengerbtn,4,0,1,1)
        grid.addWidget(datelabel,4,1)
        grid.addWidget(self.datetext,4,2)
        self.setLayout(grid)

        #connect buttons to other window
        routesbtn.clicked.connect(self.Routes)
        stopsbtn.clicked.connect(self.Stops)
        vehiclesbtn.clicked.connect(self.Vehicles)
        passengerbtn.clicked.connect(self.Passenger)

    def Routes(self):
        self.dbwindow = DatabaseWindow(self)
        self.dbwindow.routes()
        self.dbwindow.show()
        self.close()

    def Stops(self):
        self.dbwindow = DatabaseWindow1(self)
        self.dbwindow.show()
        self.close()
    def Vehicles(self):
        self.dbwindow = DatabaseWindow2(self)
        self.dbwindow.show()
        self.close()
    def Passenger(self):
        self.dbwindow = DatabaseWindow(self)
        self.dbwindow.show()
        self.close()

class DatabaseWindow(QWidget):
    def __init__(self,main):
        super(DatabaseWindow,self).__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 200
        self.main = main
        okButton = QPushButton("ok")

        grid = QGridLayout()
        grid.addWidget(okButton,0,0)
        grid.addWidget(self.initUI(),1,0)
        self.setLayout(grid)
        okButton.clicked.connect(self.back)



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
       # Create table

        cursor = connection.cursor()
        cursor.execute("select * from routes")
        datalist = []
        for row in cursor:
            datalist.append(row)

        rows = len(datalist)
        column = len(datalist[0].keys())
        keys = []
        for entry in datalist[0].keys():
            keys.append(entry)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(column)

        self.tableWidget.setHorizontalHeaderLabels(keys)

        for i in range(rows):
            for n in range(len(datalist[0].keys())):
                self.tableWidget.setItem(i,n, QTableWidgetItem(f"{datalist[i][list(datalist[0].keys())[n]]}"))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
    def back(self):
        self.main.show()
        self.close()

    def routes(self):
        tablename = 'routes'
        self.tablename = ''
        print(self.tablename)


















        # table selection change
        #self.tableWidget.doubleClicked.connect(self.on_click)

# class DatabaseWindow(QWidget):
#     def __init__(self,main):
#         super(DatabaseWindow,self).__init__()
#         self.setWindowTitle("Database")
#         self.main = main

#         #okButton = QPushButton("Ok")
#         cursor = connection.cursor()
#         cursor.execute("select * from routes")


#         table_model = SimpleTableModel(dict(cursor).keys(), dict(cursor).values())
#         table_view = QTableView()
#         table_view.setModel(table_model)

#         self.vbox = QVBoxLayout()
#         sekf,addWidget()

#         # grid = QGridLayout()
#         # grid.addWidget(okButton,0,0)
#         # grid.addWidget(table_view,1,0)
#         # self.setLayout(grid)
#         #okButton.clicked.connect(self.back)
#     def back(self):
#         self.main.show()
#         self.close()


#     def createtable(self):
#         cursor = connection.cursor()
#         cursor.execute("select * from routes")
#         for row in cursor:
#             print(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    global connection
    connection = pymysql.connect(host='localhost',user='root',db = 'marta',password = '',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    main.show()
    sys.exit(app.exec_())
