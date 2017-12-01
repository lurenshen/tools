#coding=utf-8

#处理数据类型sheettype4, 该类型为sheettype2的数组形式
from . import hdl_number
from . import hdl_table
from . import hdl_bool
from . import hdl_string
from . import hdl_language
import re

sub_indent = "\t\t" #子表解析时缩进
third_indent = "\t\t\t" #三级缩进
fn_idx = 2 #字段名所在行
ft_idx = 3 #字段类型所在行
data_begin_row = 4
data_begin_col = 2

#row_index_格式为"xxxxx_,nnn_", nnn_为table_name
def handle_sheettype4(book_, row_index_, sheet_name_):
    pass
    # sheettype4_str = sub_indent + "sheettype4_str,\n"
    split_list = row_index_.split(",", 1)
    table_name = split_list[1]
    is_tn_a_num = re.match(r"\d+$", table_name) and True or False
    if is_tn_a_num:
        table_name = "[%s]" % table_name

    sheettype4_str = ""
    if table_name == "":
        sheettype4_str = sub_indent + "{\n"
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st4(sheet, row_index_)
        sheettype4_str = sheettype4_str + sheet_str + "%s},\n" % sub_indent
    else:
        sheettype4_str = sub_indent + table_name + " = \n%s{\n" % sub_indent
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st4(sheet, row_index_)
        sheettype4_str = sheettype4_str + sheet_str + "%s},\n" % sub_indent

    return sheettype4_str

def handle_st4(sheet_, row_index_):
    pass
    # return "hello world\n"/
    total_rows = sheet_.nrows
    total_cols = sheet_.ncols
    field_name_row = sheet_.row_values(fn_idx)
    field_type_row = sheet_.row_values(ft_idx)

    st4_str = ""
    data_row_cnt = 0
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        curr_row_index = data_row[1]
        if curr_row_index != row_index_:
            continue
        else:
            if data_row_cnt <= 0:
                st4_str = "%s{\n" % third_indent
            else:
                st4_str = st4_str + "%s{\n" % third_indent

            for i in range(data_begin_col, total_cols):
                pass
                data_val = data_row[i]
                if data_val == "":
                    continue

                data_type = field_type_row[i]
                data_name = field_name_row[i]
                if data_type == data_type == "int" or data_type == "float" or data_type == "long":
                    pass
                    data_str = hdl_number.handle_number(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "bool":
                    data_str = hdl_bool.handle_bool(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "string":
                    data_str = hdl_string.handle_string(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "table":
                    data_str = hdl_table.handle_table(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "language":
                    data_str = hdl_language.handle_language(data_name, data_val, 4)
                    st4_str = st4_str + data_str
            st4_str = st4_str + "%s},\n" % third_indent
        data_row_cnt = data_row_cnt + 1

    return st4_str

