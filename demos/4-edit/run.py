# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import ui_edit

class myForm(qw.QWidget, ui_edit.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.lcdNumber.setDecMode()  #设置显示模式
        self.lcdNumber.setSegmentStyle(self.lcdNumber.Flat)
        self.lcdNumber.setDigitCount(10)
        # self.lcdNumber.setProperty()

        self.lineEdit.textChanged.connect(self.text_changed_cb)

    def text_changed_cb(self):
        value = self.lineEdit.text()
        self.lcdNumber.display(str(value))
        self.label.setText(value)

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = myForm()
    w.show()

    sys.exit(app.exec_())