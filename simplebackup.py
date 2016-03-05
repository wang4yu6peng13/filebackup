#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 简单的文件备份
import os
import time

source = ['/home/shiyanlou/Code/']
target_dir = '/home/shiyanlou/Desktop/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" % (target, ' '.join(source))
# zip命令：
# -q ： 选项用来表示zip命令安静的的工作
# -r ： 选项用来标识zip命令对目录递归的工作，即包括对该文件和其子文件操作

if os.system(zip_command) == 0:
    print('Successful backup')
else:  # 返回错误号
    print('Backup Failed')
