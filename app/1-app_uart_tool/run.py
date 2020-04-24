# encoding=utf-8

import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import PyQt5.QtGui as qg
import ui_uart_tool

import logging
import threading
from time import sleep
import serial
import serial.tools.list_ports
import tool
import utils

# sys.setrecursionlimit(1000000)

class myForm(qw.QMainWindow, ui_uart_tool.Ui_MainWindow):
    signal_recv_data = qc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("串口工具")
        self.setWindowIcon(qg.QIcon("image/uart.ico"))

        #load settings
        self.settings = qc.QSettings("config.ini", qc.QSettings.IniFormat)
        # self.com = self.settings.value("SETUP/COM_VALUE")
        self.baud = self.settings.value("SETUP/BAUD_VALUE", 0, type=int)
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
        # self.comboBox_uart.addItem(self.com)
        self.comboBox_baud.setCurrentText(str(self.baud))
        self.comboBox_databit.setCurrentText(self.databit)
        self.comboBox_polarity.setCurrentText(self.polarity)
        self.comboBox_stopbit.setCurrentText(self.stopbit)
        self.comboBox_flow.setCurrentText(self.flow)
        self.radio_recv_ascii.setChecked(True)
        self.radio_send_ascii.setChecked(True)
        self.statusbar.showMessage("status:ready")

        # signal
        self.comboBox_baud.currentIndexChanged.connect(self.combox_baud_cb)
        self.action_start.triggered.connect(self.action_start_cb)
        self.action_pause.triggered.connect(self.action_pause_cb)
        self.action_exit.triggered.connect(self.action_stop_cb)
        self.action_clear.triggered.connect(self.action_clear_cb)
        self.pushButton.clicked.connect(self.btn_send_cb)
            # self define
        self.signal_recv_data.connect(self.update_textbrowser_recv_cb)

        # logging
        logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] [%(levelname)s] %(message)s',
                filename='log',
                filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
        logger = logging.getLogger('logger')
        logger.addHandler(console)
        self.logger = logger

        # start thread listen component's status
        self.uart_run_status = 0
        self.uart_init_status = 0
        self.uart_start_status = 0

        def check_valid_uart():
            # com select
            port_values = []

            port_list = list(serial.tools.list_ports.comports())
            length = len(port_list)
            if (0 == len(port_list)):
                print("can't find serial port")
                self.comboBox_uart.setCurrentIndex(-1)
                self.comboBox_uart.clear()
            else:
                for i in range(0, len(port_list)):
                    port_values.append(port_list[i][0])
                
                for i in range(len(port_list)):
                    index = self.comboBox_uart.findText(port_values[i], qc.Qt.MatchFixedString)
                    if (index < 0):
                        current_text = self.comboBox_uart.currentText()
                        self.comboBox_uart.addItem(port_values[i])
                        if ("" == current_text):
                            # print("current text is NULL")
                            sleep(0.04)
                            self.comboBox_uart.setCurrentIndex(-1)
                        else:
                            print("current text is ", current_text)
                # remove eut
                count = self.comboBox_uart.count()
                for i in range(count):
                    data = self.comboBox_uart.itemText(i)
                    is_uart_exist = 0
                    for j in range(length):
                        if (data == port_values[j]):
                            is_uart_exist = 1
                    if (0 == is_uart_exist):
                        #remove1 
                        self.comboBox_uart.removeItem(i)
                        current_data = self.comboBox_uart.currentText()
                        if (current_data == data or current_data == ""):
                            self.comboBox_uart.clear()

        def gui_status_thread():
            print("start gui_status_thread ......")
            while (True):
                check_valid_uart()
                if ( 1== self.uart_run_status ):
                    pass
                sleep(2)
        threading.Thread(target=gui_status_thread, daemon=True).start()

        self.tool = tool.Tool(self, logger.info)  #串口工具逻辑处理对象

    def update_textbrowser_recv_cb(self, data):
        self.textBrowser_recv.insertPlainText(data)
        cursor = self.textBrowser_recv.textCursor()
        self.textBrowser_recv.moveCursor(cursor.End)

    def combox_baud_cb(self):
        self.baud = self.comboBox_baud.currentText()

    def action_start_cb(self):
        self.uart_start_status = 1
        print("action start pressed.")

    def action_stop_cb(self):
        self.uart_start_status = 0

    def action_pause_cb(self):
        self.uart_start_status = 2  # pause

    def action_clear_cb(self):
        self.textBrowser_recv.clear()

    def btn_send_cb(self):
        send_text = self.textEdit_send.toPlainText()
        self.tool.send_data_fun(send_text.encode())


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w1 = myForm()
    w1.show()

    app.exec_()