# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : data.py
# @Author: 杨崇
# @Date  : 2019/5/26
# @Desc  : null
import datetime
import time

# start_data = time.time()
# print("当前时间戳为:", start_data)
# time.sleep(2)
# end_data = time.time()
# print("当前时间戳为:", end_data)
# data = end_data - start_data
#
# print("当前时间戳为:", time.strftime("%H:%M:%S", data))


# startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(startTime)
# time.sleep(2)
# endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(endTime)
# startTime = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
# print(startTime)
# endTime = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
# # 相减得到秒数
# # 秒
# seconds = (endTime - startTime).seconds
# min = (endTime - startTime).min
# print(min)

# def test_clock():
#     start = time.perf_counter
#     time.sleep(1)
#     end = time.perf_counter
#     print("test clock():", "%fms" % ((end - start) * 1000))
#
#
# if __name__ == '__main__':
#     test_clock()
start_data = time.time()
time.sleep(2)
end_data = time.time()
data = end_data - start_data
print(data)
print(datetime.timedelta(seconds=data))
