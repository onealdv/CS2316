import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Hello PyQt!')
lbl = QLabel('Hello, label!', w)
w.show()
sys.exit(app.exec_())
