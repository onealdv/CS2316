#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Count Button')
        self.count = 0

        self.count_label = QLabel(str(self.count))
        self.inc_btn = QPushButton('Increment Count')
        self.inc_btn.clicked.connect(self.inc_count)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.inc_btn)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.count_label)

        self.setLayout(self.vbox)

    def inc_count(self):
        self.count += 1
        self.count_label.setText(str(self.count))

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
