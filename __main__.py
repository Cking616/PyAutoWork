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


def analysis_original_file(original_filename, raw_filename, target_year, target_month):
    original_file = open(original_filename)

    # current_year = 2000
    # current_month = 0
    raw_dict = defaultdict(set)
    for line in original_file:
        # line = re.sub(r'[^0-9]+', ' ', line)
        line = line.strip()
        identify, year, month, day, *rev = re.split(r'[\s-]\s*', line)
        if int(year) != target_year:
            continue
        if int(month) != target_month:
            continue
        raw_dict[identify].add(day)

    with open(raw_filename, 'wt') as raw_file:
        for key in raw_dict:
            for day in raw_dict[key]:
                txt = key + ' ' +  day + '\n'
                raw_file.write(txt)


def dat2xls(in_filename, out_filename):
    raw_file = open(in_filename)

    raw_dict = defaultdict(set)
    for line in raw_file:
        line.strip('')
        identify,  day, *rev = re.split(r'[\s-]\s*', line)
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
    analysis_original_file('D:/Downloads/1_attlog.dat', '4.txt', 2017, 4)
    dat2xls('4.txt', 'text_xls4.xls')
    pass
