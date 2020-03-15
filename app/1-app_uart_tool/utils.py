#-*- encoding: utf-8 -*-
 
import json
import sys
import binascii
from io import BytesIO
import struct
import time
import string
import datetime

def get_date_data():
    time_data = {"YEAR":10, "MONTH":10, "DAY":10}
    data = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    data_str = data.split("-")
    time_data["YEAR"] = int( data_str[0] )
    time_data["MONTH"] = int( data_str[1] )
    time_data["DAY"] = int( data_str[2] )
    return time_data

# 2019-11-13T17:01:02.000+08:00
def get_date_from_str(data):
    tm = {"YEAR":1234, "MONTH":12, "DAY":15}
    res = data.split("-")
    tm["YEAR"] = int(res[0])
    tm["MONTH"] = int(res[1])
    da = res[2]
    res = da.split("T")
    tm["DAY"] = int(res[0])

    print(tm)
    return tm

def unix_time(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))
    return timestamp


def get_timestamp_commit(data):
    res = data.split("T")
    time_str = res[0] + " 00:00:00"
    return unix_time(time_str)

def get_timestamp_now():
    tm = get_date_data()
    time_str = ("%d-%d-%d 00:00:00" % (tm["YEAR"], tm["MONTH"], tm["DAY"]) )
    return unix_time(time_str)

# # 相差一天是86400
# print(get_timestamp_commit("2019-11-13T17:01:02.000+08:00"))
# print(get_timestamp_now())

# print(get_date_data())

def get_sys_time():
    old_time = datetime.datetime.now()

    time.sleep(4)

    cur_time = datetime.datetime.now()

    secs = (cur_time - old_time).seconds

    print("time : ", cur_time - old_time)

    print("secs is ", secs)


def list_to_string(data_list):
    bydate = bytes(data_list)
    data_str = bydate.decode()
    print(data_str)
    return data_str