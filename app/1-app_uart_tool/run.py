# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import ui_uart_tool

num = 0

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = qw.QMainWindow()

    ui = ui_uart_tool.Ui_MainWindow()
    ui.setupUi(w)

    w.show()

    sys.exit(app.exec_())

