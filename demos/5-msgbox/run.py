# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import msgbox

class myForm(qw.QWidget, msgbox.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.btn_fun)

    def btn_fun(self):
        print("ready to show messagebox.")
        qw.QMessageBox.information(self, "提示", "MessageBox信息在这里~", qw.QMessageBox.Yes | qw.QMessageBox.No)

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = myForm()
    w.show()

    sys.exit(app.exec_())