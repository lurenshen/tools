# coding=utf-8

#处理数据类型"bool"

ind_level_list = ["\t", "\t\t", "\t\t\t", "\t\t\t\t", "\t\t\t\t\t"] #缩进表, indent_level_list, 分别为一级，二级，三级，四级缩进

def handle_bool(data_name_, data_val_, ind_level_, is_last_col_=False):
    pass
    # bool_str = indent_2 + "bool_str,\n"
    ind_level_idx = ind_level_ - 1
    if ind_level_idx < 0 or ind_level_idx > 5:
        print("indent level error")
        return ""

    if str(data_val_) == "1":
        data_val_ = "true"
    elif str(data_val_) == "0":
        data_val_ = "false"

    bool_str = ""
    if is_last_col_:
        bool_str = ind_level_list[ind_level_idx] + "\"%s\":\"%s\"\n" % (str(data_name_), str(data_val_))
    else:
        bool_str = ind_level_list[ind_level_idx] + "\"%s\":\"%s\",\n" % (str(data_name_), str(data_val_))

    return bool_str