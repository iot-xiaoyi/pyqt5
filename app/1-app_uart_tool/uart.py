import serial
import serial.tools.list_ports
import queue
import threading
from time import sleep
import datetime

class Uart(object):
    def __init__(self, port, baud, log):
        self.err = 0
        self.log = log
        self.list_cb = {}
        self.recv_queue = queue.Queue(10)
        self.send_queue = queue.Queue(10)

        try:
            self.uart = serial.Serial(port, baud)
            self.err = 0
            self.run_status = 1
        except:
            self.log("com init error!!!")
            self.err = -1
            self.run_status = 0
        
        def recv_data_thread():
            while True:
                try:
                    if (1 == self.run_status):
                        nums = self.uart.inWaiting()
                        if (nums > 0):
                            recv_msg = self.uart.read(nums)
                        else:
                            continue
                        if self.recv_queue.full():
                            self.recv_queue.get()
                        self.recv_queue.put(recv_msg.decode())
                        data = "[module->pc] " +str(recv_msg)
                        print(data)
                        # self.log(data)
                    sleep(0.05)
                except Exception as e:
                    self.log("Error")
                    self.log(e)

        def send_data_thread():
            while True:
                if (1 == self.run_status):
                    send_data = self.send_queue.get()
                    self.uart.write(send_data)
                else:
                    sleep(0.05)
        self.log("start send and recv data thread.")
        threading.Thread(target=recv_data_thread, daemon=True).start()
        threading.Thread(target=send_data_thread, daemon=True).start()

    def close(self):
        self.run_status = 0
        self.uart.close()

    def reopen(self, port):
        self.uart = serial.Serial(port, 115200)
        self.run_status = 1

    def flush(self):
        while not self.recv_queue.empty():
            self.recv_queue.get()
    
    def send_data_fun(self, data):
        self.send_queue.put(data)
        data = "[pc->module] " +str(data)
        print(data)
        # self.log(data)

    def get_data_from_recv_queue(self, timeout):
        old_time = datetime.datetime.now()
        cur_time = datetime.datetime.now()
        time = (cur_time - old_time).seconds
        while (time < timeout):
            if (False == self.recv_queue.empty()):
                data = self.recv_queue.get()
                return data
            cur_time = datetime.datetime.now()
            time = (cur_time-old_time).seconds
            sleep(0.01)
                
        return None

