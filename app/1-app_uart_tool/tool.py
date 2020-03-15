from time import sleep
from enum import Enum
import uart
import threading
import binascii
import numpy as np

class Tool(object):
    def __init__(self, parent, log):
        self.log = log
        self.err = -1
        self.run_status = 0
        self.parent = parent

        threading.Thread(target=self.tool_logic_thread, daemon=True).start()

    def tool_logic_thread(self):
        self.log("start tool logic thread")
        while (True):
            if (1 == self.parent.uart_start_status and 0 == self.run_status):
                port = self.parent.comboBox_uart.currentText()
                self.uart = uart.Uart(port, self.parent.baud, self.log)
                self.run_status = 1
                # start recv data thread
                threading.Thread(target=self.recv_data_thread, daemon=True).start()
            elif(2 == self.parent.uart_start_status):
                pass
            elif(0 == self.parent.uart_start_status):
                self.close_uart()
            sleep(0.1)

    def recv_data_thread(self):
        self.log("start recv_data_thread")
        while (True):
            if (False == self.uart.recv_queue.empty()):
                data = self.uart.recv_queue.get()
                self.parent.signal_recv_data.emit(data)
            sleep(0.1)

    def open_uart(self, port):
        # sleep(1)
        if (0 == self.run_status):
            try:
                self.uart = uart.Uart(port, log)
                self.err = 0
                self.run_status = 1
                # start recv data thread
                threading.Thread(target=self.recv_data_thread, daemon=True).start()
            except:
                self.err = -1
                self.run_status = 0
    
    def close_uart(self):
        if (1 == self.run_status):
            self.uart.close()
            self.run_status = 0

    def recv_data_fun(self, timeout):
        recv_list = self.uart.get_data_from_buff(timeout)
        return recv_list

    def send_data_fun(self, data):
        print("[PC->module] ", data)
        self.uart.send_data_fun(data)

