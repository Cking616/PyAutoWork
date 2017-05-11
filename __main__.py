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
import os
import os.path
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


def translate_process():
    print("�÷�����һ������dat��¼�ļ��ŵ�dat�ļ�����\n")
    input("��ɺ��밴Enter����\n")

    print("��ѡ��Ҫʹ�õ�dat�ļ�������֮ǰ�����ֺ�\n")
    dat_file_list = []
    num_of_file = 0
    for parent, dir_names, file_names in os.walk('dat'):
        for file_name in file_names:
            dat_file_list.append(file_name)
            num_of_file = num_of_file + 1
            txt = str(num_of_file) + ' ' + file_name + '\n'
            print(txt)

    input_choice = int(input("��ѡ��Ҫʹ�õ�dat�ļ�������֮ǰ�����ֺ�\n"))
    while input_choice < 1 or input_choice > num_of_file:
        input_choice = int(input("��������ֲ��ڷ�Χ�ڣ�����������\n"))
    original_filename =  './dat/'+ dat_file_list[input_choice - 1]

    input_choice = int(input("������ɸѡ�����(��Χ2000��2030)\n"))
    while input_choice < 2000 or input_choice > 2030:
        input_choice = int(input("��������ֲ��ڷ�Χ�ڣ�����������\n"))
    target_year = input_choice

    input_choice = int(input("������ɸѡ���·�(��Χ1��12)\n"))
    while input_choice < 1 or input_choice > 12:
        input_choice = int(input("��������ֲ��ڷ�Χ�ڣ�����������\n"))
    target_month = input_choice

    raw_filename = './txt/' + str(target_year) + '-' + str(target_month) + '.txt'
    xls_filename = './excel/' + str(target_year) + '-' + str(target_month) + '.xls'

    txt = "��txt�ļ���������" + raw_filename + '\n'
    print(txt)

    txt = "����excel�ļ�������" + raw_filename + '\n'
    print(txt)
    analysis_original_file(original_filename, raw_filename, target_year, target_month)
    dat2xls(raw_filename, xls_filename)


if __name__ == '__main__':
    translate_process()
    input("�밴Enter������\n")
