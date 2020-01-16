# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
import ui_test

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = qw.QMainWindow()

    ui = ui_test.Ui_MainWindow()
    ui.setupUi(w)

    # set icon and window's title
    w.setWindowTitle("测试V1.0")
    w.setWindowIcon(qg.QIcon("icons/umbrella.ico"))

    w.show()

    sys.exit(app.exec_())

