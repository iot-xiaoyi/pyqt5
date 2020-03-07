# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import prettytable as pt
import ui_chart

# sys.setrecursionlimit(1000000)

class myForm(qw.QMainWindow, ui_chart.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # init gui
        self.statusbar.showMessage("status:ok")
        self.pushButton.clicked.connect(self.btn_test_cb)

    def btn_test_cb(self):
        tb = pt.PrettyTable()
        tb.field_names = ["姓名", "语文", "数学", "英语"]
        tb.add_row(["王二", 80, 90, 70])
        tb.add_row(["李三", 85, 95, 80])
        tb.add_row(["赵四", 90, 75, 86])
        print(tb)
        text_data = str(tb)
        self.textBrowser.insertPlainText(text_data)
        self.textBrowser.insertPlainText("\r\n")

        self.textBrowser.insertPlainText("clear_rows后数据如下\r\n")
        tb.clear_rows()
        print(tb)
        text_data = str(tb)
        self.textBrowser.insertPlainText(text_data)

        self.textBrowser.insertPlainText("\r\n重新add_row后数据如下\r\n")
        tb.add_row(["刘无", 85, 95, 80])
        tb.add_row(["杨六", 90, 75, 86])
        print(tb)
        text_data = str(tb)
        self.textBrowser.insertPlainText(text_data)

        self.textBrowser.insertPlainText("\r\nclear后数据如下\r\n")
        tb.clear()
        print(tb)
        text_data = str(tb)
        self.textBrowser.insertPlainText(text_data)

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w1.show()

    app.exec_()