# coding=utf-8

#处理基本的数据类型["int", "float", "long"]

ind_level_list = ["\t", "\t\t", "\t\t\t", "\t\t\t\t", "\t\t\t\t\t"] #缩进表, indent_level_list, 分别为一级，二级，三级，四级缩进

def handle_number(data_name_, data_val_, ind_level_, is_last_col_=False):
    pass
    # number_str = indent_2 + "number_str,\n"
    ind_level_idx = ind_level_ - 1
    if ind_level_idx < 0 or ind_level_idx > 5:
        print("indent level error")
        return ""

    number_str = ""
    if is_last_col_:
        number_str = ind_level_list[ind_level_idx] + "\"%s\":\"%s\"\n" % (str(data_name_), str(data_val_))
    else:
        number_str = ind_level_list[ind_level_idx] + "\"%s\":\"%s\",\n" % (str(data_name_), str(data_val_))

    return number_str
