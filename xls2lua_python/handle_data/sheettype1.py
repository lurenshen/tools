#coding=utf-8

#处理数据类型sheettype1
from . import hdl_number
from . import hdl_table
from . import hdl_bool
from . import hdl_string
from . import hdl_language

sub_indent = "\t\t" #子表解析时缩进
third_indent = "\t\t\t" #三级缩进
type_row_idx = 1
data_begin_col = 2
data_begin_row = 4
fn_idx = 2 #字段名所在行
ft_idx = 3 #字段类型所在行

#sheet相当于一个特殊的table
def handle_sheettype1(book_, row_index_, sheet_name_, table_name_):
    pass
    # sheettype1_str = ind_level_list[1] + "sheettype1_str,\n"
    sheettype1_str = ""
    if table_name_ == "":
        sheettype1_str = sub_indent + "{\n"
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st1(sheet, row_index_)
        sheettype1_str = sheettype1_str + sheet_str + "%s},\n" % sub_indent
    else:
        sheettype1_str = sub_indent + table_name_ + " = \n%s{\n" % sub_indent
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st1(sheet, row_index_)
        sheettype1_str = sheettype1_str + sheet_str + "%s},\n" % sub_indent

    return sheettype1_str

#handle_sheettype1
def handle_st1(sheet_, row_index_):
    pass
    # return "handle_sheettype1"
    total_rows = sheet_.nrows
    total_cols = sheet_.ncols
    type_val_row = sheet_.row_values(type_row_idx)
    type_name = type_val_row[1]
    field_type_row = sheet_.row_values(ft_idx) #字段类型
    field_name_row = sheet_.row_values(fn_idx)

    st1_str = ""
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        curr_row_idx = data_row[1]
        if curr_row_idx != row_index_:
            continue
        else:
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
                    type_str = hdl_number.handle_number(type_name, type_val, 4)
                    val_str = hdl_number.handle_number(data_name, data_val, 4)
                    st1_str = st1_str + "%s{\n%s%s%s},\n" % (third_indent, type_str, val_str, third_indent)
                elif data_type == "string":
                    type_str = hdl_number.handle_number(type_name, type_val, 4)
                    val_str = hdl_string.handle_string(data_name, data_val, 4)
                    st1_str = st1_str + "%s{\n%s%s%s},\n" % (third_indent, type_str, val_str, third_indent)
                elif data_type == "bool":
                    type_str = hdl_number.handle_number(type_name, type_val, 4)
                    val_str = hdl_bool.handle_bool(data_name, data_val, 4)
                    st1_str = st1_str + "%s{\n%s%s%s},\n" % (third_indent, type_str, val_str, third_indent)
                elif data_type == "table":
                    type_str = hdl_number.handle_number(type_name, type_val, 4)
                    val_str = hdl_table.handle_table(data_name, data_val, 4)
                    st1_str = st1_str + "%s{\n%s%s%s},\n" % (third_indent, type_str, val_str, third_indent)
                elif data_type == "language":
                    type_str = hdl_number.handle_number(type_name, type_val, 4)
                    val_str = hdl_language.handle_language(data_name, data_val, 4)
                    st1_str = st1_str + "%s{\n%s%s%s},\n" % (third_indent, type_str, val_str, third_indent)

    return st1_str
