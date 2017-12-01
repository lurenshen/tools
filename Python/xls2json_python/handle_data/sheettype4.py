#coding=utf-8

#处理数据类型sheettype4, 该类型为sheettype2的数组形式
from . import hdl_number
from . import hdl_table
from . import hdl_bool
from . import hdl_string
from . import hdl_language
from . import sheet_com
import re

sub_indent = "\t\t" #子表解析时缩进
third_indent = "\t\t\t" #三级缩进
fn_idx = 2 #字段名所在行
ft_idx = 3 #字段类型所在行
data_begin_row = 4
data_begin_col = 2

#row_index_格式为"xxxxx_,nnn_", nnn_为table_name
def handle_sheettype4(book_, row_index_, sheet_name_, is_last_col_=False):
    pass
    # sheettype4_str = sub_indent + "sheettype4_str,\n"
    split_list = row_index_.split(",", 1)
    table_name = split_list[1]

    sheettype4_str = ""
    if table_name == "":
        print("handle_sheettype1:table_name_ can not be null, table_name_ = [%s]" % table_name_)
        return ""
    else:
        sheettype4_str = sub_indent + "\"%s\":\n%s[\n" % (table_name, sub_indent)
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st4(sheet, row_index_)
        if is_last_col_:
            sheettype4_str = sheettype4_str + sheet_str + "%s]\n" % sub_indent
        else:
            sheettype4_str = sheettype4_str + sheet_str + "%s],\n" % sub_indent

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
    need_total_rows = sheet_com.cal_need_total_rows(sheet_, row_index_)
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        curr_row_index = data_row[1]
        if curr_row_index != row_index_:
            continue
        else:
            need_total_cols = sheet_com.cal_need_total_cols(data_row, total_cols)
            if data_row_cnt <= 0:
                st4_str = "%s{\n" % third_indent
            else:
                st4_str = st4_str + "%s{\n" % third_indent

            data_row_cnt = data_row_cnt + 1
            data_col_cnt = 0
            for i in range(data_begin_col, total_cols):
                pass
                data_val = data_row[i]
                if data_val == "":
                    continue

                data_col_cnt = data_col_cnt + 1
                data_type = field_type_row[i]
                data_name = field_name_row[i]
                if data_type == "int" or data_type == "float" or data_type == "long":
                    if data_col_cnt >= need_total_cols:
                        data_str = hdl_number.handle_number(data_name, data_val, 4, True)
                    else:
                        data_str = hdl_number.handle_number(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "bool":
                    if data_col_cnt >= need_total_cols:
                        data_str = hdl_bool.handle_bool(data_name, data_val, 4, True)
                    else:
                        data_str = hdl_bool.handle_bool(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "string":
                    if data_col_cnt >= need_total_cols:
                        data_str = hdl_string.handle_string(data_name, data_val, 4, True)
                    else:
                        data_str = hdl_string.handle_string(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "table":
                    if data_col_cnt >= need_total_cols:
                        data_str = hdl_table.handle_table(data_name, data_val, 4, True)
                    else:
                        data_str = hdl_table.handle_table(data_name, data_val, 4)
                    st4_str = st4_str + data_str
                elif data_type == "language":
                    if data_col_cnt >= need_total_cols:
                        data_str = hdl_language.handle_language(data_name, data_val, 4, True)
                    else:
                        data_str = hdl_language.handle_language(data_name, data_val, 4)
                    st4_str = st4_str + data_str
            if data_row_cnt >= need_total_rows:
                st4_str = st4_str + "%s}\n" % third_indent
            else:
                st4_str = st4_str + "%s},\n" % third_indent

    return st4_str

