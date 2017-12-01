#coding=utf-8

#处理数据类型sheettype2
from . import hdl_number
from . import hdl_table
from . import hdl_bool
from . import hdl_string
from . import hdl_language

sub_indent = "\t\t" #子表解析时缩进
fn_idx = 2 #字段名所在行
ft_idx = 3 #字段类型所在行
data_begin_row = 4
data_begin_col = 2

def handle_sheettype2(book_, row_index_, sheet_name_, table_name_, is_last_col_=False):
    pass
    # sheettype2_str = ind_level_list[1] + "sheettype2_str,\n"
    sheettype2_str = ""
    if table_name_ == "":
        print("handle_sheettype2:table_name_ can not be null, table_name_ = [%s]" % table_name_)
        return ""
    else:
        sheettype2_str = sub_indent + "\"%s\":\n%s{\n" % (table_name_, sub_indent)
        sheet = book_.sheet_by_name(sheet_name_)
        sheet_str = handle_st2(sheet, row_index_)
        if is_last_col_:
            sheettype2_str = sheettype2_str + sheet_str + "%s}\n" % sub_indent
        else:
            sheettype2_str = sheettype2_str + sheet_str + "%s},\n" % sub_indent

    return sheettype2_str

def handle_st2(sheet_, row_index_):
    pass
    # return "handle_sheettype1\n"
    total_rows = sheet_.nrows
    total_cols = sheet_.ncols
    field_name_row = sheet_.row_values(fn_idx)
    field_type_row = sheet_.row_values(ft_idx)

    st2_str = ""
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        curr_row_id = data_row[1]
        if curr_row_id != row_index_:
            continue
        else:
            for i in range(data_begin_col, total_cols):
                pass
                data_val = data_row[i]
                if data_val == "":
                    continue

                data_type = field_type_row[i]
                data_name = field_name_row[i]
                if data_type == data_type == "int" or data_type == "float" or data_type == "long":
                    pass
                    if i == total_cols - 1:
                        data_str = hdl_number.handle_number(data_name, data_val, 3, True)
                    else:
                        data_str = hdl_number.handle_number(data_name, data_val, 3)
                    st2_str = st2_str + data_str
                elif data_type == "bool":
                    if i == total_cols - 1:
                        data_str = hdl_bool.handle_bool(data_name, data_val, 3, True)
                    else:
                        data_str = hdl_bool.handle_bool(data_name, data_val, 3)
                    st2_str = st2_str + data_str
                elif data_type == "string":
                    if i == total_cols - 1:
                        data_str = hdl_string.handle_string(data_name, data_val, 3, True)
                    else:
                        data_str = hdl_string.handle_string(data_name, data_val, 3)
                    st2_str = st2_str + data_str
                elif data_type == "table":
                    if i == total_cols - 1:
                        data_str = hdl_table.handle_table(data_name, data_val, 3, True)
                    else:
                        data_str = hdl_table.handle_table(data_name, data_val, 3)
                    st2_str = st2_str + data_str
                elif data_type == "table":
                    if i == total_cols - 1:
                        data_str = hdl_language.handle_language(data_name, data_val, 3, True)
                    else:
                        data_str = hdl_language.handle_language(data_name, data_val, 3)
                    st2_str = st2_str + data_str

    return st2_str
