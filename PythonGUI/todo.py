#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QListView,
    QLineEdit
)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Todo List")

        self.list_view = QListView()
        self.list_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.list_model)

        self.line_edit = QLineEdit()
        self.add_button = QPushButton("Add")
        self.add_button.setEnabled(False)

        self.add_button.clicked.connect(self.add_todo_item)
        self.line_edit.textChanged.connect(self.enable_add_button)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.list_view)
        self.vbox.addWidget(self.line_edit)
        self.vbox.addWidget(self.add_button)
        self.setLayout(self.vbox)

    def add_todo_item(self):
        list_item = QStandardItem(self.line_edit.text())
        self.list_model.appendRow(list_item)
        self.line_edit.setText('')
        self.line_edit.setFocus()

    def enable_add_button(self):
        if len(self.line_edit.text()) == 0:
            self.add_button.setEnabled(False)
        else:
            self.add_button.setEnabled(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
