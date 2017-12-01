#coding=utf-8

#处理数据类型sheettype5, 该类型为sheettype1的数组形式
from . import hdl_number
from . import hdl_table
from . import hdl_bool
from . import hdl_string
from . import hdl_language
import re

sub_indent = "\t\t" #子表解析时缩进
third_indent = "\t\t\t" #三级缩进
fourth_indent = "\t\t\t\t" #四级缩进
type_row_idx = 1
data_begin_col = 2
data_begin_row = 4
fn_idx = 2 #字段名所在行
ft_idx = 3 #字段类型所在行

def handle_sheettype5(book_, row_index_, sheet_name_):
    pass
    # sheettype5_str = sub_indent + "sheettype5_str,\n"
    split_list = row_index_.split(",", 1)
    table_name = split_list[1]
    is_tn_a_num = re.match(r"\d+$", table_name) and True or False
    if is_tn_a_num:
        table_name = "[%s]" % table_name

    sheettype5_str = ""
    if table_name == "":
        sheettype5_str = sub_indent + "{\n"
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st5(sheet, row_index_)
        sheettype5_str = sheettype5_str + sheet_str + "%s},\n" % sub_indent
    else:
        sheettype5_str = sub_indent + table_name + "=\n%s{\n" % sub_indent
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st5(sheet, row_index_)
        sheettype5_str = sheettype5_str + sheet_str + "%s},\n" % sub_indent

    return sheettype5_str

def handle_st5(sheet_, row_index_):
    pass
    # return "hello world\n"
    total_rows = sheet_.nrows
    total_cols = sheet_.ncols
    type_val_row = sheet_.row_values(type_row_idx)
    type_name = type_val_row[1]
    field_type_row = sheet_.row_values(ft_idx) #字段类型
    field_name_row = sheet_.row_values(fn_idx)

    st5_str = ""
    data_row_cnt = 0
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        curr_row_idx = data_row[1]
        if curr_row_idx != row_index_:
            continue
        else:
            if data_row_cnt <= 0:
                st5_str = "%s{\n" % third_indent
            else:
                st5_str = st5_str + "%s{\n" % third_indent

            for i in range(data_begin_col, total_cols):
                pass
                data_val = data_row[i]
                if data_val == "":
                    continue

                data_type = field_type_row[i]
                data_name = field_name_row[i]
                type_val = type_val_row[i]
                if data_type == "int" or data_type == "float" or data_type == "long":
                    pass
                    type_str = hdl_number.handle_number(type_name, type_val, 5)
                    val_str = hdl_number.handle_number(data_name, data_val, 5)
                    st5_str = st5_str + "%s{\n%s%s%s},\n" % (fourth_indent, type_str, val_str, fourth_indent)
                elif data_type == "string":
                    type_str = hdl_number.handle_number(type_name, type_val, 5)
                    val_str = hdl_string.handle_string(data_name, data_val, 5)
                    st5_str = st5_str + "%s{\n%s%s%s},\n" % (fourth_indent, type_str, val_str, fourth_indent)
                elif data_type == "bool":
                    type_str = hdl_number.handle_number(type_name, type_val, 5)
                    val_str = hdl_bool.handle_bool(data_name, data_val, 5)
                    st5_str = st5_str + "%s{\n%s%s%s},\n" % (fourth_indent, type_str, val_str, fourth_indent)
                elif data_type == "table":
                    type_str = hdl_number.handle_number(type_name, type_val, 5)
                    val_str = hdl_table.handle_table(data_name, data_val, 5)
                    st5_str = st5_str + "%s{\n%s%s%s},\n" % (fourth_indent, type_str, val_str, fourth_indent)
                elif data_type == "language":
                    type_str = hdl_number.handle_number(type_name, type_val, 4)
                    val_str = hdl_language.handle_language(data_name, data_val, 4)
                    st5_str = st5_str + "%s{\n%s%s%s},\n" % (third_indent, type_str, val_str, third_indent)
            st5_str = st5_str + "%s},\n" % third_indent
        data_row_cnt = data_row_cnt + 1

    return st5_str

