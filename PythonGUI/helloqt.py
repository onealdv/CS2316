import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('Hello, Oneal!')
w.show()
return_code = app.exec_()
sys.exit(return_code)
