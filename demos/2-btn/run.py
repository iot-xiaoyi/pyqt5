# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import ui_btn

num = 0

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = qw.QMainWindow()

    ui = ui_btn.Ui_MainWindow()
    ui.setupUi(w)
    ui.lcdNumber.setDecMode()  #设置显示模式
    ui.lcdNumber.setStyleSheet("border:2pxsolidgreen;color:red;background:silver;")
    ui.lcdNumber.setSegmentStyle(ui.lcdNumber.Flat)

    def lcd_show():
        global num
        num = num + 1
        ui.lcdNumber.display(num)

    ui.pushButton.clicked.connect(lcd_show)
    w.show()

    sys.exit(app.exec_())

