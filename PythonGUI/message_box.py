import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Message Box Demo")
        left, top, width, height = 50, 50, 300, 200
        self.setGeometry(left, top, width, height)

        info_btn = QPushButton("Information ...", self)
        info_btn.move(50, 50)
        info_btn.resize(info_btn.sizeHint())
        info_btn.clicked.connect(self.show_information_box)

        question_btn = QPushButton("Question ...", self)
        question_btn.move(100, 100)
        question_btn.resize(info_btn.sizeHint())
        question_btn.clicked.connect(self.show_question_box)


    def show_information_box(self):
        reply = QMessageBox.information(self,
                                        "Message Box Title",
                                        "The message.",
                                        QMessageBox.Ok)

    def show_question_box(self):
        reply = QMessageBox.question(self,
                                     "Question",
                                     "CS 2316 is the best, right?!",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        answer = "Yes" if reply == QMessageBox.Yes else "No"
        self.statusBar().showMessage("Question box reply: " + answer)

if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
