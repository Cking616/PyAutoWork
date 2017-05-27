# -*- coding:gbk -*-

"""
@version: 1.0
@license: Apache Licence 
@author:  kht,cking616
@contact: cking616@mail.ustc.edu.cn
@software: PyCharm Community Edition
@file: attendance.py
@time: 2017/5/27 13:44
"""
from selenium import webdriver


class Attendance:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://172.16.3.241:8060')
        driver = self.driver
        driver.find_element_by_id("txt_username").send_keys('674')
        driver.find_element_by_id("txt_pwd").send_keys('cking616')
        driver.find_element_by_id("ddd").click()
        driver.get('http://172.16.3.241:8060/employeeConsols/index_emp.aspx')

    def get_exception_record(self):
        driver = self.driver
        driver.find_element_by_link_text('')


if __name__ == '__main__':
    my_attendance = Attendance()
