#coding=utf-8

import sys
import time
import codecs

import global_var as gvar
import global_func as gfunc

import handle_basic as dt_basic

#####################常量部分########################

#导出部分
ROW_FIELD_NAME = 1                  # 字段名所在行索引

#数据部分
ROW_DATA_BEGIN = 2                  # 真正数据所在行索引
COL_DATA_BEGIN = 0                  # 真正数据所在列索引

#####################变量部分########################


'''
功能 处理某个表格
参数 workbook_ 需要处理的book
参数 output_path_ 写入文件的文件夹所在
参数 postfix_ 文件名后缀
'''
def handle_workbook(workbook_, output_path_, postfix_):
    sheet_names = workbook_.sheet_names()
    main_sheet = workbook_.sheet_by_name(sheet_names[0]) #默认读取第1个Sheet

    #文件名
    file_path = "%s/%s.%s" % (output_path_, sheet_names[0], postfix_)

    #是否添加引号
    gvar.set('need_quot', True)

    #是否压缩
    gvar.set('need_zip', False)

    #
    gvar.set('total_rows', main_sheet.nrows)
    gvar.set('total_cols', main_sheet.ncols)

    print("%s(%d,%d,%s,%s)" % (file_path, gvar.get('total_rows'), gvar.get('total_cols'), gvar.get('need_quot'), gvar.get('need_zip')))

    #
    rd_field_name = main_sheet.row_values(ROW_FIELD_NAME)

    #文件头
    file_content = "{%s" % gfunc.get_crlf(1)

    #数据
    for x in range(ROW_DATA_BEGIN, main_sheet.nrows):
        rowdata = main_sheet.row_values(x)
        #过滤注释行
        val = str(rowdata[0])
        if val.startswith('//'):
            continue

        #
        is_last_row = (x == main_sheet.nrows - 1)  #是否为最后一行
        file_content += handle_one_row_data(workbook_, rowdata, rd_field_name, is_last_row)

    #文件尾
    file_content += "}%s" % gfunc.get_crlf(1)

    # 写文件
    output_file = codecs.open(file_path, "w", "utf-8")
    output_file.write(file_content)

'''
功能 处理一行数据
参数 workbook_ 需要处理的book
参数 rowdata_ 一行所有数据
参数 rd_field_name_ 字段名字所有数据
参数 is_last_row_ 是否为最后一行
返回 处理后的字符串
'''
def handle_one_row_data(workbook_, rowdata_, rd_field_name_, is_last_row_):
    # print("handle_one_row_data %s" % rowdata_)
    # print("handle_one_row_data %s" % rd_field_name_)
    # print("is_last_row_ = %d" % is_last_row_)

    #
    indent = gfunc.get_indent(1)    #\t
    crlf = gfunc.get_crlf(1)        #\n

    #
    ret_str = indent                        #返回的本行数据
    cols_cnt = 0                            #已经处理的列数
    need_cols = 0                           #需要处理的列数
    total_cols = gvar.get('total_cols')     #总共的列数

    #统计需要处理的导出列
    for x in range(COL_DATA_BEGIN, total_cols):
        need_cols += 1
    
    for x in range(COL_DATA_BEGIN, total_cols):
        #
        cols_cnt += 1
        #是否最后一列
        is_last_col = (cols_cnt >= need_cols)
        
        #过滤注释列
        field_name = str(rd_field_name_[x])
        if field_name.startswith('//'):
            continue

        #过滤数据为空列
        data_val = rowdata_[x]
        if str(data_val) == "":
            continue

        #是否为数字
        if gfunc.isnumber(data_val):
            data_val = int(data_val)

        #"key":{}
        if x == COL_DATA_BEGIN:
            data_str = "%s\"%s\":%s%s{%s" % (indent, data_val, crlf, indent, crlf)

        #
        data_str += dt_basic.handle_basic(field_name, data_val, 2, is_last_col)

    #
    data_str += "%s}%s%s" % (indent, gfunc.get_comma(is_last_row_), crlf)
    return data_str
