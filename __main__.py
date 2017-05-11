# -*- coding: gbk -*-

"""
@version: 1.0
@license: Apache Licence 
@author:  kht,cking616
@contact: cking616@mail.ustc.edu.cn
@software: PyCharm Community Edition
@file: __main__.py
@time: 2017/5/11 9:08
"""
import re
from collections import defaultdict
import xlwt


def analysis_original_file():
    pass


def dat2xls(in_filename, out_filename):
    raw_file = open(in_filename)

    raw_dict = defaultdict(set)
    for line in raw_file:
        line.strip('\t')
        identify, month, day, *rev = re.split(r'[\s-]\s*', line)
        raw_dict[identify].add(day)

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

    for i in range(1, 32):
        worksheet.write(0, i + 1, i)

    for key in raw_dict:
        index = int(key) + 2
        worksheet.write(index, 0, int(key))
        for day in raw_dict[key]:
            worksheet.write(index, int(day) + 1, '\u221a')

    if not out_filename.endswith('.xls'):
        out_filename = out_filename + '.xls'
    workbook.save(out_filename)


if __name__ == '__main__':
    dat2xls('D:/Downloads/4.txt', 'text_xls.xls')
    pass
