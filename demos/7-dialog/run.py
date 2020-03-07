# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import dialog
import dialog_new

# sys.setrecursionlimit(1000000)

class myForm(qw.QWidget, dialog.Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def close_w1(self):
        self.close()

class myFormNew(qw.QWidget, dialog_new.Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w2 = myFormNew()
    w1.show()
    def show_w2():
        w2.show()

    # w1.pushButton.clicked.connect(w1.close_w1)
    w1.pushButton.clicked.connect(show_w2)

    app.exec_()