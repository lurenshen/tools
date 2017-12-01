#coding=utf-8

#处理数据类型sheettype3
from . import hdl_number
from . import hdl_table
from . import hdl_bool
from . import hdl_string
from . import hdl_language

sub_indent = "\t\t" #子表解析时缩进
third_indent = "\t\t\t" #三级缩进
fn_idx = 2 #字段名所在行
ft_idx = 3 #字段类型所在行
data_begin_row = 4
data_begin_col = 2

def handle_sheettype3(book_, row_index_, sheet_name_, table_name_):
    pass
    # sheettype3_str = indent_2 + "sheettype3_str,\n"
    sheettype3_str = ""
    if table_name_ == "":
        sheettype3_str = sub_indent + "{\n"
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st3(sheet, row_index_)
        sheettype3_str = sheettype3_str + sheet_str + "%s},\n" % sub_indent
    else:
        sheettype3_str = sub_indent + table_name_ + " = \n%s{\n" % sub_indent
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st3(sheet, row_index_)
        sheettype3_str = sheettype3_str + sheet_str + "%s},\n" % sub_indent

    return sheettype3_str

def handle_st3(sheet_, row_index_):
    pass
    # return sub_indent + "handle_sheettype1\n"
    total_rows = sheet_.nrows
    total_cols = sheet_.ncols
    field_name_row = sheet_.row_values(fn_idx)
    field_type_row = sheet_.row_values(ft_idx)

    st3_str = ""
    data_row_cnt = 0
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        curr_row_idx = data_row[1]
        if curr_row_idx != row_index_:
            continue
        else:
            if data_row_cnt <= 0: #可能含有多条数据
                st3_str = "%s{\n" % third_indent
            else:
                st3_str = st3_str + "%s{\n" % third_indent

            for i in range(data_begin_col, total_cols):
                pass
                data_val = data_row[i]
                if data_val == "":
                    continue

                data_name = field_name_row[i]
                data_type = field_type_row[i]
                if data_type == "int" or data_type == "float" or data_type == "long":
                    data_str = hdl_number.handle_number(data_name, data_val, 4)
                    st3_str = st3_str + data_str
                elif data_type == "string":
                    data_str = hdl_string.handle_string(data_name, data_val, 4)
                    st3_str = st3_str + data_str
                elif data_type == "bool":
                    data_str = hdl_bool.handle_bool(data_name, data_val, 4)
                    st3_str = st3_str + data_str
                elif data_type == "table":
                    data_str = hdl_table.handle_table(data_name, data_val, 4)
                    st3_str = st3_str + data_str
                elif data_type == "table":
                    data_str = hdl_language.handle_language(data_name, data_val, 4)
                    st3_str = st3_str + data_str
            st3_str = st3_str + "%s},\n" % third_indent
        data_row_cnt = data_row_cnt + 1

    return st3_str