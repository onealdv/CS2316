import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp,
    QAction,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QRadioButton,
    QGridLayout)
#    QLineEdit textbox ,QPushButton Button,QComboBox Drop Down,

class LoginWindow(QWidget): #every window is a new class
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setWindowTitle("Login")

        #defining different elements
        unlabel = QLabel("Username")
        pwlabel = QLabel("Password")
        self.usernameText = QLineEdit() #textbox
        self.passwordText = QLineEdit()
        loginButton = QPushButton("Login")
        registerButton = QPushButton("Register")

        #put into grid layout
        grid = QGridLayout()
        grid.addWidget(unlabel,1,0)
        grid.addWidget(pwlabel,2,0) #2,0 is the grid coordinate position
        grid.addWidget(self.usernameText,1,1)
        grid.addWidget(self.passwordText,2,1)
        grid.addWidget(loginButton,3,0,1,2) #the extra 1 and 2 is button takes up 1 row and 2 columns width
        grid.addWidget(registerButton,4,0,1,2)

        self.setLayout(grid)

        loginButton.clicked.connect(self.Login)
        registerButton.clicked.connect(self.Register)

    def Login(self):
        print("Login")

    def Register(self):
        self.regwindow = RegistrationWindow(self)
        self.regwindow.show()
        self.close()

class RegistrationWindow(QWidget):
    def __init__(self,main): #main allows the window to know where it came from
        super(RegistrationWindow,self).__init__()
        self.setWindowTitle("Register")
        self.main = main

        backButton = QPushButton("Back")
        grid = QGridLayout()
        grid.addWidget(backButton,0,0)

        self.setLayout(grid)

        backButton.clicked.connect(self.back)

    def back(self):
        self.main.show() #shows previous window
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = LoginWindow()
    mainWindow.show()
    sys.exit(app.exec_())

