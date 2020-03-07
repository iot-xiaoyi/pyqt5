# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import ui_settings

# sys.setrecursionlimit(1000000)

class myForm(qw.QMainWindow, ui_settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #load settings
        qc.QSettings()
        self.settings = qc.QSettings("config.ini", qc.QSettings.IniFormat)
        self.com = self.settings.value("SETUP/COM_VALUE")
        self.baud = self.settings.value("SETUP/BAUD_VALUE")
        self.databit = self.settings.value("SETUP/DATABIT_VALUE")
        self.polarity = self.settings.value("SETUP/POLARITY_VALUE")
        # odd even  none
        if (self.polarity == "odd"):
            self.polarity = "奇校验"
        elif(self.polarity == "even"):
            self.polarity = "偶校验"
        elif(self.polarity == "none"):
            self.polarity = "无"
        self.stopbit = self.settings.value("SETUP/STOPBIT_VALUE")
        self.flow =  self.settings.value("SETUP/FLOW_VALUE")
        if (self.flow == "cts"):
            self.flow =  "RTS/CTS"
            print("odd check taest")
        elif(self.flow == "xon"):
            self.flow =  "XON/XOFF"
        elif(self.flow == "none"):
            self.flow =  "无"

        #init gui
        self.comboBox_uart.addItem(self.com)
        self.comboBox_baud.setCurrentText(self.baud)
        self.comboBox_databit.setCurrentText(self.databit)
        self.comboBox_polarity.setCurrentText(self.polarity)
        self.comboBox_stopbit.setCurrentText(self.stopbit)
        self.comboBox_flow.setCurrentText(self.flow)
        self.statusbar.showMessage("status:ok")

        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)
        self.pushButton.clicked.connect(self.btn_test_cb)

    def combox_baud_cb(self):
        self.baud = self.comboBox_baud.currentText()

    def btn_test_cb(self):
        self.settings.setValue("SETUP/BAUD_VALUE", self.baud)
        qw.QMessageBox.information(self, "提示", "QSettings保存成功")


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w1.show()

    app.exec_()