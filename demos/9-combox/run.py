# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import ui_combox

# sys.setrecursionlimit(1000000)

class myForm(qw.QMainWindow, ui_combox.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statusbar.showMessage("status:ok")

        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)
        self.pushButton.clicked.connect(self.btn_test_cb)

    def combox_baud_cb(self):
        data = self.comboBox_baud.currentText()
        qw.QMessageBox.information(self, "提示", "您选择了" + data)

    def btn_test_cb(self):
        print("hello world")
        self.comboBox_uart.addItem("COM4")


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w1.show()

    app.exec_()