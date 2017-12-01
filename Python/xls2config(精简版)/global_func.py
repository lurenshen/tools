#coding=utf-8

import global_var as gvar

'''
获取缩进(\t)
如果压缩则返回空
参数 max_ 拼接的个数
'''
def get_indent(max_=1):
    need_zip = gvar.get('need_zip')
    if need_zip:
        return ""
    else:
        ret = ""
        for x in range(0,max_):
            ret += "\t"
        return ret 

'''
获取回车换行(\n)
如果压缩则返回空
参数 max_ 拼接的个数
'''
def get_crlf(max_=1):
    need_zip = gvar.get('need_zip')
    if need_zip:
        return ""
    else:
        ret = ""
        for x in range(0,max_):
            ret += "\n"
        return ret

'''
获取引号("\"")
设置不用引号则返回
参数 isforce_ 是否强制有引号，比如string类型
'''
def get_quot(isforce_=False):
    if isforce_:
        return "\""

    need_quot = gvar.get('need_quot')
    if need_quot:
        return "\""
    else:
        return ""

'''
获取逗号(,)
最后一行或最后一列没有逗号
参数 islast_ 是否最后一个
'''
def get_comma(islast_=False):
    return "" if islast_ else ","

'''
判断是否为数字
'''
def isnumber(str_):
    try:
        float(str_)
        return True
    except:
        return False
