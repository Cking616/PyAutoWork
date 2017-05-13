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


def generate_style():
    borders = xlwt.Borders()  # Create Borders
    borders.left = xlwt.Borders.THIN
    """
    # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, 
    MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    """
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40

    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    """
    # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, 
      HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    """
    alignment.vert = xlwt.Alignment.VERT_CENTER
    # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

    font = xlwt.Font()
    font.name = 'SimSun'  # ָ�������塱

    style = xlwt.XFStyle()  # Create Style
    style.borders = borders  # Add Borders to Style
    style.alignment = alignment  # Add Alignment to Style
    style.font = font
    return style


def analysis_original_file(original_filename, raw_filename, target_year, target_month):
    original_file = open(original_filename)
    work_day = set()
    raw_dict = defaultdict(set)
    for line in original_file:
        line = line.strip()
        split_list = re.split(r'[\s-]\s*', line)
        identify = split_list[0]
        year = split_list[1]
        month = split_list[2]
        day = split_list[3]
        if int(year) != target_year:
            continue
        if int(month) != target_month:
            continue
        raw_dict[identify].add(day)
        work_day.add(int(day))

    with open(raw_filename, 'wt') as raw_file:
        for key in raw_dict:
            for day in raw_dict[key]:
                txt = key + ' ' + day + '\n'
                raw_file.write(txt)
    return work_day


def dat2xls(in_filename, out_filename, work_day):
    raw_file = open(in_filename)
    style = generate_style()

    raw_dict = defaultdict(set)
    for line in raw_file:
        line.strip('')
        split_list = re.split(r'[\s-]\s*', line)
        identify = split_list[0]
        day = split_list[1]
        raw_dict[int(identify)].add(int(day))

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

    index = 2
    for i in work_day:
        worksheet.write(2, index, i, style)
        index = index + 1
    txt = 'ȱϯ'.decode('gbk')
    worksheet.write(2, index,  txt, style)

    index = 3
    while len(raw_dict) != 0:
        key = min(raw_dict.keys())
        worksheet.write(index, 0, key, style)
        worksheet.write(index, 1, ' ', style)
        y = 2
        for i in work_day:
            if i in raw_dict[key]:
                worksheet.write(index, y, '\u221a'.decode('unicode-escape'), style)
            else:
                worksheet.write(index, y, ' ', style)
            y = y + 1
        worksheet.write(index, y, ' ', style)
        raw_dict.pop(key)
        index = index + 1

    txt = '����'.decode('gbk')
    worksheet.write_merge(1, 2, 0, 0, txt, style)  # Merges row 0's columns 0 through 3.
    txt = '����'.decode('gbk')
    worksheet.write_merge(1, 2, 1, 1,  txt, style)  # Merges row 0's columns 0 through 3.
    lens = len(work_day)
    txt = '�������'.decode('gbk')
    worksheet.write_merge(1, 1, 2, lens + 2,  txt, style)  # Merges row 1 through 2's columns 0 through 3.
    txt = '����ϵͳ¼��'.decode('gbk')
    worksheet.write_merge(0, 0, 0, lens + 2,  txt, style)  # Merges row 1 through 2's columns 0 through 3.
    if not out_filename.endswith('.xls'):
        out_filename = out_filename + '.xls'
    workbook.save(out_filename)


def translate_process():
    print("�÷�����һ������dat��¼�ļ��ŵ���ǰĿ¼�����ɵ�dat�ļ�����\n".decode('gbk'))
    if not os.path.exists('dat'):
        os.mkdir('dat')
    if not os.path.exists('excel'):
        os.mkdir('excel')
    if not os.path.exists('txt'):
        os.mkdir('txt')
    raw_input("��ɺ��밴Enter����\n".decode('gbk'))

    print("��ѡ��Ҫʹ�õ�dat�ļ�������֮ǰ�����ֺ�\n".decode('gbk'))
    dat_file_list = []
    num_of_file = 0
    for parent, dir_names, file_names in os.walk('dat'):
        for file_name in file_names:
            dat_file_list.append(file_name)
            num_of_file = num_of_file + 1
            txt = str(num_of_file) + ' ' + file_name + '\n'
            print(txt)

    input_choice = int(raw_input("��ѡ��Ҫʹ�õ�dat�ļ�������֮ǰ�����ֺ�\n".decode('gbk')))
    while input_choice < 1 or input_choice > num_of_file:
        input_choice = int(raw_input("��������ֲ��ڷ�Χ�ڣ�����������\n".decode('gbk')))
    original_filename = './dat/' + dat_file_list[input_choice - 1]

    input_choice = int(raw_input("������ɸѡ�����(��Χ2000��2030)\n".decode('gbk')))
    while input_choice < 2000 or input_choice > 2030:
        input_choice = int(raw_input("��������ֲ��ڷ�Χ�ڣ�����������\n".decode('gbk')))
    target_year = input_choice

    print("����Ϊѭ��ѡ��0�˳�".decode('gbk'))
    while input_choice != 0:
        input_choice = int(raw_input("������ɸѡ���·�(��Χ1��12),����0�˳�\n".decode('gbk')))
        if input_choice == 0:
            break
        while input_choice < 1 or input_choice > 12:
            input_choice = int(raw_input("��������ֲ��ڷ�Χ�ڣ�����������\n".decode('gbk')))
        target_month = input_choice

        raw_filename = './txt/' + str(target_year) + '-' + str(target_month) + '.txt'
        xls_filename = './excel/' + str(target_year) + '-' + str(target_month) + '.xls'

        txt = "��txt�ļ���������".decode('gbk') + raw_filename + '\n'
        print(txt)

        txt = "����excel�ļ�������".decode('gbk') + raw_filename + '\n'
        print(txt)
        work_day = analysis_original_file(original_filename, raw_filename, target_year, target_month)
        dat2xls(raw_filename, xls_filename, work_day)


if __name__ == '__main__':
    translate_process()
    raw_input("�밴Enter������\n".decode('gbk'))