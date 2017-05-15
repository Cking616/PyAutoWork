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
import json
import time
import os
import pyperclip


def ask4set_clipboard(filename):
    with open(filename, 'w') as file:
        data = {'command': 'set_clipboard'}
        json.dump(data, file)


def get_clipboard_text():
    text = pyperclip.paste()
    return str(text)


def set_clipboard_text(text):
    pyperclip.copy(text)


def clipboard2indoor_net():
    os.chdir(r'\\172.16.1.111\公网至内网文件\kanghaitao康海涛')
    with open(r'\\172.16.1.111\公网至内网文件\kanghaitao康海涛\pub_net_clipboard.txt', 'wb') as file:
        text = get_clipboard_text()
        file.write(text.encode('utf-8'))
        ask4set_clipboard('1.json')


def get_pub_net_clipboard():
    with open(r'\\172.16.10.123\02.公网至内网文件\kanghaitao康海涛\pub_net_clipboard.txt', 'rb') as file:
        text = str(file.read(), encoding='utf-8')
        set_clipboard_text(text)


class IndoorNetDaemon:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            os.chdir(r'\\172.16.10.123\02.公网至内网文件\kanghaitao康海涛')
            json_list = [name for name in os.listdir(r'\\172.16.10.123\02.公网至内网文件\kanghaitao康海涛')
                         if name.endswith('.json')]
            for filename in json_list:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    if data['command'] == 'set_clipboard':
                        get_pub_net_clipboard()
                os.remove(filename)

            time.sleep(1)


if __name__ == '__main__':
    clipboard2indoor_net()
    # process = IndoorNetDaemon()
    # process.run()

