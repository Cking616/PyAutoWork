# -*- coding:gbk -*-

"""
@version: 1.0
@license: Apache Licence 
@author:  kht,cking616
@contact: cking616@mail.ustc.edu.cn
@software: PyCharm Community Edition
@file: simpleoa.py
@time: 2017/5/27 15:16
"""
from selenium import webdriver


class SimpleOA:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://172.16.1.166:85')
        driver = self.driver
        driver.find_element_by_id("loginid").send_keys('kanghaitao')
        driver.find_element_by_id("userpassword").send_keys('kht@cking616')
        driver.find_element_by_id("login").click()

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    my_attendance = SimpleOA()
