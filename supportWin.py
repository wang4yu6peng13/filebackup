#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 备份文件：支持Windows目录的分隔符 \
# 日期文件夹 存放 时间压缩包
import os
import time

# 基本变量
source = ["/home/shiyanlou/Code/"]
target_dir = "/home/shiyanlou/Desktop/"

today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime("%H%M%S")

touch = today_dir + os.sep + time_dir + '.zip'
command_touch = "zip -qr " + touch + ' ' + ' '.join(source)

# 逻辑思路判断
if not os.path.exists(today_dir):  # 目标文件夹不存在
    os.makedirs(today_dir)
if os.system(command_touch) == 0:
    print('Success backup Up')
else:
    print('Failed backup')
