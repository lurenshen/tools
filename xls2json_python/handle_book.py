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

import time

#行数都是从0开始计算的
fd_idx = 2 #字段描述所在行
fn_idx = 3 #字段名所在行
ft_idx = 4 #字段类型所在行
need_conv_idx = 1 #该行记录是否需要转成lua/json
data_begin_row = 6 #配置数据开始所在行
data_begin_col = 1 #配置数据开始所在列
main_indent = "\t" #主表解析时的缩进

'''
book_:需要处理的book
output_path_:写入文件的文件夹所在
'''
def handle_workbook(book_, output_path_):
    pass
    sheet_names = book_.sheet_names()
    main_sheet = book_.sheet_by_name(sheet_names[0]) #get "主表"

    file_name = main_sheet.cell_value(0, 1)
    whole_file_name = "%s%s.json" % (output_path_, file_name)
    output_file = open(whole_file_name, "w")

    fd_row = main_sheet.row_values(fd_idx)
    fn_row = main_sheet.row_values(fn_idx)
    ft_row = main_sheet.row_values(ft_idx)
    need_conv_row = main_sheet.row_values(need_conv_idx)

    total_rows = main_sheet.nrows
    total_cols = main_sheet.ncols

    file_content = "{\n"
    for x in range(data_begin_row, total_rows):
        pass
        one_row_data = main_sheet.row_values(x)
        if x == total_rows - 1: #处理最后一行
            data_str = handle_one_row_data(one_row_data, need_conv_row, fn_row, ft_row, total_cols, book_, True)
        else:
            data_str = handle_one_row_data(one_row_data, need_conv_row, fn_row, ft_row, total_cols, book_)
        file_content = file_content + data_str

    file_content = file_content + "}\n"
    # print file_head
    # print file_content
    output_file.write(file_content)

#统计需要转json的列数
def cal_neet_trans_cols(need_conv_row_, row_data_, total_cols):
    pass
    temp_list = []
    for x in range(data_begin_col, total_cols):
        pass
        if "C" in need_conv_row_[x] and row_data_[x] != "":
            pass
            temp_list.append(x)

    return len(temp_list)

#功能: 处理一行数据，返回处理后的字符串
def handle_one_row_data(row_data_, need_conv_row_, row_name_, row_type_, data_col_, book_, is_last_row_=False):
    pass
    # return "\thello world\n"

    row_index = row_data_[1]
    data_str = main_indent
    cols_cnt = 0 #已经处理的列数
    need_cols = cal_neet_trans_cols(need_conv_row_, row_data_, data_col_)
    # print("need_cols = %d"%need_cols)
    # print(need_conv_row_)
    # print("need_cols = %d" % need_cols)
    for x in range(data_begin_col, data_col_):
        pass
        need_conv_flag = need_conv_row_[x]
        if "C" not in need_conv_flag: #没有"C"标志，不用处理
            continue

        data_val = row_data_[x]
        if data_val == "": #数据为空，不用处理
                continue

        cols_cnt = cols_cnt + 1
        data_type = row_type_[x]
        data_name = row_name_[x]
        if x == data_begin_col:
            pass
            data_str = "%s\"%s\":\n%s{\n" % (main_indent, data_val, main_indent)

        if data_type == "int" or data_type == "float" or data_type == "long":
            if cols_cnt >= need_cols: #处理最后一列
                number_str = hdl_number.handle_number(data_name, data_val, 2, True)
            else:
                number_str = hdl_number.handle_number(data_name, data_val, 2)
            data_str = data_str + number_str
        elif data_type == "string":
            if cols_cnt >= need_cols: #处理最后一列
                string_str = hdl_string.handle_string(data_name, data_val, 2, True)
            else:
                string_str = hdl_string.handle_string(data_name, data_val, 2)
            data_str = data_str + string_str
        elif data_type == "bool":
            if cols_cnt >= need_cols: #处理最后一列
                bool_str = hdl_bool.handle_bool(data_name, data_val, 2, True)
            else:
                bool_str = hdl_bool.handle_bool(data_name, data_val, 2)
            data_str = data_str + bool_str
        elif data_type == "table":
            if cols_cnt >= need_cols: #处理最后一列
                table_str = hdl_table.handle_table(data_name, data_val, 2, True)
            else:
                table_str = hdl_table.handle_table(data_name, data_val, 2)
            data_str = data_str + table_str.encode("utf-8")
        elif data_type == "language":
            if cols_cnt >= need_cols: #处理最后一列
                language_str = hdl_language.handle_language(data_name, data_val, 2)
            else:
                language_str = hdl_language.handle_language(data_name, data_val, 2, True)
            data_str = data_str + language_str.encode("utf-8")
        elif data_type == "sheettype1":
            if cols_cnt >= need_cols: #处理最后一列
                sheettype1_str = sheettype1.handle_sheettype1(book_, row_index, data_val, data_name, True)
            else:
                sheettype1_str = sheettype1.handle_sheettype1(book_, row_index, data_val, data_name)
            data_str = data_str + sheettype1_str
        elif data_type == "sheettype2":
            if cols_cnt >= need_cols: #处理最后一列
                sheettype2_str = sheettype2.handle_sheettype2(book_, row_index, data_val, data_name, True)
            else:
                sheettype2_str = sheettype2.handle_sheettype2(book_, row_index, data_val, data_name)
            data_str = data_str + sheettype2_str
        elif data_type == "sheettype3":
            if cols_cnt >= need_cols: #处理最后一列
                sheettype3_str = sheettype3.handle_sheettype3(book_, row_index, data_val, data_name, True)
            else:
                sheettype3_str = sheettype3.handle_sheettype3(book_, row_index, data_val, data_name)
            data_str = data_str + sheettype3_str
        elif data_type == "sheettype4":
            if cols_cnt >= need_cols: #处理最后一列
                sheettype4_str = sheettype4.handle_sheettype4(book_, data_val, data_name, True)
            else:
                sheettype4_str = sheettype4.handle_sheettype4(book_, data_val, data_name)
            data_str = data_str + sheettype4_str
        elif data_type == "sheettype5":
            if cols_cnt >= need_cols: #处理最后一列
                sheettype5_str = sheettype5.handle_sheettype5(book_, data_val, data_name, True)
            else:
                sheettype5_str = sheettype5.handle_sheettype5(book_, data_val, data_name)
            data_str = data_str + sheettype5_str
        else:
            # print "data_type error, data_type = %s\n" % data_type
            continue

    if is_last_row_:
        data_str = data_str + "%s}\n" % main_indent
    else:
        data_str = data_str + "%s},\n" % main_indent

    return data_str

