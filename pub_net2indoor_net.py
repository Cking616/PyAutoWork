# -*- coding: utf-8 -*-
"""
@version: 1.0
@author: kht
@license: Apache Licence 
@author: kht(cking616)
@contact: cking616@mail.ustc.edu.cn
@software: PyCharm Community Edition
@file: pub_net2indoor_net.py
@time: 2017/5/14 0014 19:11
@brief：公网至内网传输文件
"""
import shutil
import sys
import os.path
import pyperclip


def get_clipboard_text():
    text = pyperclip.paste()
    return text


def set_clipboard_text(text):
    pyperclip.set_clipboard(text)


def clipboard2indoor_net():
    with open(r'\\172.16.1.111\公网至内网文件\kanghaitao康海涛\pub_net_clipboard.txt', 'wt') as file:
        text = (get_clipboard_text())
        file.write(text)


def get_pub_net_clipboard():
    with open(r'\\172.16.10.123\公网至内网文件\kanghaitao康海涛\pub_net_clipboard.txt', 'rt') as file:
        text = file.read()
        set_clipboard_text(text)


if __name__ == '__main__':
    clipboard2indoor_net()
