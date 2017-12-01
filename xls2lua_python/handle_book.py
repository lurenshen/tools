#coding=utf-8

from handle_data import hdl_number
from handle_data import hdl_table
from handle_data import hdl_bool
from handle_data import hdl_string
from handle_data import sheettype1
from handle_data import sheettype2
from handle_data import sheettype3
from handle_data import sheettype4
from handle_data import sheettype5
from handle_data import hdl_language
from handle_data import lang_package

import time
import os

#行数都是从0开始计算的
fd_idx = 2 #字段描述所在行
fn_idx = 3 #字段名所在行
ft_idx = 4 #字段类型所在行
need_conv_idx = 1 #该行记录是否需要转成lua/json
data_begin_row = 6 #配置数据开始所在行
data_begin_col = 1 #配置数据开始所在列
main_indent = "\t" #主表解析时的缩进
file_name_col = 1 #分文件处理中子文件名所在列
lang_sheet_name = "语言包" #语言包的sheet_name

'''
book_:需要处理的book
output_path_:写入文件的文件夹所在
'''
def handle_workbook(book_, output_path_):
    pass
    sheet_names = book_.sheet_names()
    main_sheet = book_.sheet_by_name(sheet_names[0]) #get "主表"
    if handle_need_generate_lang(sheet_names): #处理语言包
        lang_sheet = book_.sheet_by_name(lang_sheet_name)
        lang_package.handle_lang_package(lang_sheet, output_path_)

    table_name = main_sheet.cell_value(0, 2)
    file_name = main_sheet.cell_value(0, 1)
 
    fd_row = main_sheet.row_values(fd_idx)
    fn_row = main_sheet.row_values(fn_idx)
    ft_row = main_sheet.row_values(ft_idx)
    need_conv_row = main_sheet.row_values(need_conv_idx)
    file_head = handle_file_head(fd_row, fn_row, ft_row)
    whole_file_name = "%s%s.lua" % (output_path_, file_name)

    total_rows = main_sheet.nrows
    total_cols = main_sheet.ncols
    is_only_one_row_data = False
    if total_rows - data_begin_row == 1:
        is_only_one_row_data = True

    sub_dir_name = ""
    if total_cols > 3:
        sub_dir_name = main_sheet.cell_value(0, 3)   #如果该字段不为空,则需要分文件处理;

    if sub_dir_name != "": #需要分文件处理，则分为一个主文件和一个文件夹下面诸多子文件
        handle_total_file(main_sheet, whole_file_name, file_head)
        handle_split_file(book_, main_sheet, output_path_, sub_dir_name)
    else:
        output_file = open(whole_file_name, "w")
        file_content = table_name + "=\n{\n"
        for x in range(data_begin_row, total_rows):
            pass
            one_row_data = main_sheet.row_values(x)
            data_str = handle_one_row_data(one_row_data, need_conv_row, fn_row, ft_row, total_cols, book_, is_only_one_row_data)
            file_content = file_content + data_str

        file_content = file_content + "}\n"
        # print file_head
        # print file_content
        output_file.write(file_head)
        output_file.write("\n")
        output_file.write(file_content)
        output_file.close()

#判断是否需要生产语言包
def handle_need_generate_lang(sheet_names_):
    pass
    for x in range(len(sheet_names_)):
        pass
        if sheet_names_[x] == lang_sheet_name:
            return True

    return False

#处理分文件中的诸多子文件
def handle_split_file(book_, main_sheet_, output_path_, dir_name_):
    pass
    sub_dir = output_path_ + dir_name_
    if not os.path.isdir(sub_dir):
        os.mkdir(sub_dir)

    total_rows = main_sheet_.nrows
    total_cols = main_sheet_.ncols
    fn_row = main_sheet_.row_values(fn_idx)
    ft_row = main_sheet_.row_values(ft_idx)
    need_conv_row = main_sheet_.row_values(need_conv_idx)
    file_names = main_sheet_.col_values(file_name_col)
    for x in range(data_begin_row, total_rows):
        pass
        one_row_data = main_sheet_.row_values(x)
        data_str = handle_one_row_data(one_row_data, need_conv_row, fn_row, ft_row, total_cols, book_, False, True)
        split_file_name = "%s/%s.lua" % (sub_dir, file_names[x])
        split_file = open(split_file_name, "w")
        split_file.write(data_str)
        split_file.close()

#处理分文件中的主文件入口
def handle_total_file(main_sheet_, total_file_name_, file_head_):
    pass
    total_rows = main_sheet_.nrows
    table_name = main_sheet_.cell_value(0, 2)
    sub_dir_name = main_sheet_.cell_value(0, 3)
    file_names = main_sheet_.col_values(file_name_col)

    file_content = "\n%s=\n{\n" % table_name
    for x in range(data_begin_row, total_rows):
        pass
        file_content = file_content + "--#include \"%s\\%s.lua\"\n" % (sub_dir_name, file_names[x])
    file_content = file_content + "}\n"
    # print(file_content)

    total_file = open(total_file_name_, "w")
    total_file.write(file_head_)
    total_file.write(file_content)
    total_file.close()

'''
fd_row:字段描述 field describe
fn_row:字段名 field name
ft_row:字段类型 field type
'''
def handle_file_head(fd_row_, fn_row_, ft_row_):
    pass
    fh_des = "--Automatic generation of files do not manually edit：%s\n"
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    fh_des = fh_des % curr_time
    fh_des = fh_des + "--#include \"..\..\language\LangCode.txt\" once\n"

    fd_row_str = handle_one_row_2_str(fd_row_)
    fh_des = fh_des + fd_row_str   #函数返回的字符串需要进行encode

    fn_row_str = handle_one_row_2_str(fn_row_)
    fh_des = fh_des + fn_row_str

    ft_row_str = handle_one_row_2_str(ft_row_)
    fh_des = fh_des + ft_row_str
    
    return fh_des

#功能: 将一个row list转成str, 主要用于处理文件头
def handle_one_row_2_str(one_row_):
    pass
    row_str = "--" + one_row_[0] + " "
    for x in range(len(one_row_)):
        pass
        if x != 0:
            row_str = str(row_str) + str(one_row_[x]) + " "

    row_str = row_str + "\n"

    return row_str

#功能: 处理一行数据，返回处理后的字符串
def handle_one_row_data(row_data_, need_conv_row_, row_name_, row_type_, 
                        data_col_, book_, only_one_row_data_=False, is_split_file=False):
    pass
    # return "\thello world\n"

    row_index = row_data_[1]
    data_str = main_indent
    for x in range(data_begin_col, data_col_):
        pass
        need_conv_flag = need_conv_row_[x]
        if "S" not in need_conv_flag: #没有"S"标志，不用处理
            continue

        data_val = row_data_[x]
        data_name = row_name_[x]
        if data_val == "": #数据为空，不用处理
            continue

        data_type = row_type_[x]
        if x == data_begin_col and not only_one_row_data_:
            pass
            data_str = ""
            if is_split_file: #如果是分文件处理，不需要table_name
                pass
                data_str = data_str + "%s{\n" % main_indent
            else:
                if data_type == "int":
                    pass
                    data_str = data_str + "%s[%s]=\n%s{\n" % (main_indent, data_val, main_indent)
                else:
                    data_str = data_str + "%s%s=\n%s{\n" % (main_indent, data_val, main_indent)

        if data_name == "": #数据名为空，不处理
            continue

        if data_type == "int" or data_type == "float" or data_type == "long":
            number_str = hdl_number.handle_number(data_name, data_val, 2)
            data_str = data_str + number_str
        elif data_type == "string":
            string_str = hdl_string.handle_string(data_name, data_val, 2)
            data_str = data_str + string_str
        elif data_type == "bool":
            bool_str = hdl_bool.handle_bool(data_name, data_val, 2)
            data_str = data_str + bool_str
        elif data_type == "table":
            table_str = hdl_table.handle_table(data_name, data_val, 2)
            data_str = data_str + table_str
        elif data_type == "language":
            language_str = hdl_language.handle_language(data_name, data_val, 2)
            data_str = data_str + language_str
        elif data_type == "sheettype1":
            sheettype1_str = sheettype1.handle_sheettype1(book_, row_index, data_val, data_name)
            data_str = data_str + sheettype1_str
        elif data_type == "sheettype2":
            sheettype2_str = sheettype2.handle_sheettype2(book_, row_index, data_val, data_name)
            data_str = data_str + sheettype2_str
        elif data_type == "sheettype3":
            sheettype3_str = sheettype3.handle_sheettype3(book_, row_index, data_val, data_name)
            # print(sheettype3_str)
            data_str = data_str + sheettype3_str
        elif data_type == "sheettype4":
            sheettype4_str = sheettype4.handle_sheettype4(book_, data_val, data_name)
            data_str = data_str + sheettype4_str
        elif data_type == "sheettype5":
            sheettype5_str = sheettype5.handle_sheettype5(book_, data_val, data_name)
            data_str = data_str + sheettype5_str
        else:
            # print "data_type error, data_type = %s\n" % data_type
            continue

        # print(data_str)
    if not only_one_row_data_:
        data_str = data_str + "%s},\n" % main_indent

    return data_str

