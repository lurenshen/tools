# coding=utf-8

#处理基本的数据类型，number和string
import re

ind_level_list = ["\t", "\t\t", "\t\t\t", "\t\t\t\t", "\t\t\t\t\t", "\t\t\t\t\t"] #缩进表, indent_level_list, 分别为一级，二级，三级，四级缩进

def handle_table(data_name_, data_val_, ind_level_):
    pass
    # table_str = ind_level_list[1] + "table_str,\n"
    # data_val_ = re.sub("},{", "},\n\t\t\t{", data_val_)
    ind_level_idx = ind_level_ - 1
    if ind_level_idx < 0 or ind_level_idx > 5:
        print("indent level error")
        return ""

    table_str = ""
    if data_name_ == "":
        table_str = ind_level_list[ind_level_idx] + "{\n"
        table_str = table_str + ind_level_list[ind_level_idx+1] + str(data_val_) + "\n%s},\n" % ind_level_list[ind_level_idx]
    else:
        table_str = ind_level_list[ind_level_idx] + data_name_ + " = \n%s{\n" % ind_level_list[ind_level_idx]
        table_str = table_str + ind_level_list[ind_level_idx+1] + str(data_val_) + "\n%s},\n" % ind_level_list[ind_level_idx]

    table_str = re.sub(r"},{", "},\n%s{" % ind_level_list[ind_level_idx+1], table_str)

    return table_str
