# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import ui_stack

class myForm(qw.QWidget, ui_stack.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton1.clicked.connect(self.btn1_fun)
        self.pushButton2.clicked.connect(self.btn2_fun)
        self.pushButton3.clicked.connect(self.btn3_fun)

    def btn1_fun(self):
        self.stackedWidget.setCurrentIndex(0)

    def btn2_fun(self):
        self.stackedWidget.setCurrentIndex(1)

    def btn3_fun(self):
        self.stackedWidget.setCurrentIndex(2)

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = myForm()
    w.show()

    sys.exit(app.exec_())