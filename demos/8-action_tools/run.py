# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import ui_action_tool

# sys.setrecursionlimit(1000000)

class myForm(qw.QMainWindow, ui_action_tool.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statusbar.showMessage("status:ok")

        self.action_start.triggered.connect(self.action_start_cb)
        self.action_pause.triggered.connect(self.action_pause_cb)
        self.action_exit.triggered.connect(self.action_exit_cb)
        self.action_clear.triggered.connect(self.action_clear_cb)

    def action_start_cb(self):
        qw.QMessageBox.information(self, "提示", "您点击了Start")

    def action_pause_cb(self):
        qw.QMessageBox.information(self, "提示", "您点击了Pause")

    def action_exit_cb(self):
        qw.QMessageBox.information(self, "提示", "您点击了Stop")

    def action_clear_cb(self):
        qw.QMessageBox.information(self, "提示", "您点击了clear")

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w1.show()

    app.exec_()