#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    qApp,
    QMessageBox,
    QAction
)

from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        left, top, width, height = 100, 100, 300, 200
        self.setGeometry(left, top, width, height)
        self.setWindowTitle('Quit button')
        self.create_menu_bar()

    def create_menu_bar(self):
        exit = QAction("Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip("Exit quitter")
        exit.triggered.connect(QCoreApplication.instance().quit)

        menu_bar = self.menuBar()
        # Some platforms (notably, macOS) won't work right without this:
        menu_bar.setNativeMenuBar(False)

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(exit)


    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     "Confirm",
                                     "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
