# coding=utf-8

import global_var as gvar
import global_func as gfunc

'''
基础数据类型(basic)
    bool、int、float、long、string
'''

#
def handle_basic(data_name_, data_val_, indent_level_, is_last_col_=False):
    indent = gfunc.get_indent(indent_level_)    # 缩进
    quot = gfunc.get_quot(True)                 # 引号
    comma = gfunc.get_comma(is_last_col_)       # 逗号
    crlf  = gfunc.get_crlf(1)                   # 回车换行

    #"key":"value"
    ret_str = "%s\"%s\":%s%s%s%s%s" % (indent, data_name_, quot, data_val_, quot, comma, crlf)
    return ret_str
