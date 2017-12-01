# coding=utf-8

#处理数据类型"string"

ind_level_list = ["\t", "\t\t", "\t\t\t", "\t\t\t\t", "\t\t\t\t\t"] #缩进表, indent_level_list, 分别为一级，二级，三级，四级缩进

def handle_string(data_name_, data_val_, ind_level_):
    pass
    # string_str = indent_2 + "string_str,\n"
    ind_level_idx = ind_level_ - 1
    if ind_level_idx < 0 or ind_level_idx > 5:
        print("indent level error")
        return ""

    string_str = ind_level_list[ind_level_idx] + str(data_name_) + " = \"%s\"" % str(data_val_) + ",\n"

    return string_str