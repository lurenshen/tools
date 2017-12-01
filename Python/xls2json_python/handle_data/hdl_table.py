# coding=utf-8

#处理基本的数据类型，number和string
'''
table两种形式：
key_val:"id=1,name="name""或者"{id=1,name="name"},{id=2,name="name2"}", 前一种统一转成"id=1,name="name""处理
非key_val:"1,2,3"
'''
import re

ind_level_list = ["\t", "\t\t", "\t\t\t", "\t\t\t\t", "\t\t\t\t\t", "\t\t\t\t\t"] #缩进表, indent_level_list, 分别为一级，二级，三级，四级缩进

def handle_table(data_name_, data_val_, ind_level_, is_last_col_=False):
    pass
    ind_level_idx = ind_level_ - 1
    if ind_level_idx < 0 or ind_level_idx > 5:
        print("indent level error")
        return ""

    #将table内容转成json格式
    if "{" not in str(data_val_) and "=" not in str(data_val_):
        data_val_ = ind_level_list[ind_level_idx+1] + str(data_val_)
    else:
        data_val_list = data_val_to_list(str(data_val_))
        data_val_ = proc_data_list(data_val_list, ind_level_)

    table_str = ""
    if data_name_ == "":
        print("handle_table:data_name can not be null, data_name = [%s]" % data_name_)
        return ""
    else:
        table_str = ind_level_list[ind_level_idx] + "\"%s\":\n%s[\n" % (data_name_, ind_level_list[ind_level_idx])
        if is_last_col_:
            table_str = table_str + str(data_val_) + "\n%s]\n" % ind_level_list[ind_level_idx]
        else:
            table_str = table_str + str(data_val_) + "\n%s],\n" % ind_level_list[ind_level_idx]

    table_str = re.sub(r"},{", "},\n%s{" % ind_level_list[ind_level_idx+1], table_str)

    return table_str

def data_val_to_list(data_val_):
    pass
    data_str_list = []
    if "{" not in data_val_ and "=" in data_val_:
        data_val_ = "{%s}" % data_val_
        data_str_list.append(data_val_)
    else:
        f_all = re.findall("},{", data_val_)
        group_len = len(f_all)
        group_cnt = group_len + 1
        group_re = "({.*}),?" * group_cnt
        mat = re.search(group_re, data_val_)
        for x in range(1,group_cnt+1):
            pass
            data_str_list.append(mat.group(x))

    return data_str_list

def proc_data_list(data_list_, ind_level_):
    pass
    l_len = len(data_list_)
    curr_cnt = 0
    json_str = ""
    for x in range(len(data_list_)):
        pass
        data_str = data_list_[x]
        data_str = re.sub(r"\"", "", data_str)
        key_val_list = re.findall(r"\w+", data_str)
        curr_cnt = curr_cnt + 1
        keyval_str = trans_keyval_to_json(key_val_list)
        if curr_cnt >= l_len:
            json_str = json_str + "%s%s" % (ind_level_list[ind_level_+1], keyval_str)
        else:
            json_str = json_str + "%s%s,\n" % (ind_level_list[ind_level_+1], keyval_str)

    return json_str

def trans_keyval_to_json(list):
    pass
    keyval_str = ""
    l_len = len(list)
    if l_len <= 0 or l_len%2 != 0:
        print("list error, l_len = %d" % l_len)
    else:
        total_cnt = l_len / 2
        curr_cnt = 0
        for x in range(0, l_len, 2):
            pass
            key = list[x]
            val = list[x+1]
            # print("key = %s, val = %s" % (key, val))
            curr_cnt = curr_cnt + 1
            if curr_cnt >= total_cnt:
                keyval_str = keyval_str + "\"%s\":\"%s\"" % (key, val)
            else:
                keyval_str = keyval_str + "\"%s\":\"%s\"," % (key, val)

    return "{%s}" % keyval_str

