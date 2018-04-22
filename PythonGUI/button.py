#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def up():
    print("up!")

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Hello PyQt!')
btn = QPushButton('Push it ...', w)
btn.clicked.connect(lambda: print('real good!'))
btn.clicked.connect(up)

btn2 = QPushButton('2: Push it ...', w)
btn2.clicked.connect(lambda: print('real bad!'))
btn2.clicked.connect(up)
btn2.clicked.connect(up)
w.show()
sys.exit(app.exec_())
