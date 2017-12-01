#coding=utf-8

import xlrd
import os

'''
用于测试xlrd.book.Book对象常用的一些方法
'''

#xlrd and Book
# book_xlrd = xlrd.open_workbook(".\input\singleTab.xls")
# 如果文件名中包含中文，则需要进行转码，不然读取失败,文件名开头如果有数字，需要使用转义字符'\'
filename = ".\input\\001.xls"
# filename = filename.decode('utf-8')
try:
    book_xlrd = xlrd.open_workbook(filename)
except:
    print "open_workbook error, filename: '%s'" % filename
else:
    #-----------book-----begin---------
    #sheet_names
    sheet_names = book_xlrd.sheet_names()
    print sheet_names
    for x in xrange(len(sheet_names)):
        pass
        print sheet_names[x]
    #sheet_names 和中文sheet名比较
    if sheet_names[0] == unicode("主表","utf-8"): #需要unicode
        pass
        print "%r = '主表'" % sheet_names[0]  #打印utf-8格式的字符串需要用%r
    #sheet_names 和非中文sheet名比较
    s_name = "Sheet1"
    if sheet_names[2] == s_name.decode("utf-8"): #不需要unicode,但也可以进行转码
        pass
        print "%r = 'Sheet1'" % sheet_names[0]  #打印utf-8格式的字符串需要用%r
    #sheets()  Returns:	A list of all sheets in the book. All sheets not already loaded will be loaded.
    print book_xlrd.sheets()
    #sheet_by_index(sheetx)  Parameters: sheetx – Sheet index in range(nsheets). Returns: A Sheet.
    print book_xlrd.sheet_by_index(0)
    #sheet_by_name(sheet_name)  Parameters:	sheet_name – Name of the sheet required.  Returns:	A Sheet.
    print book_xlrd.sheet_by_name(sheet_names[0])
    #nsheets = 0  The number of worksheets present in the workbook file. This information is available even when no sheets have yet been loaded.
    print book_xlrd.nsheets
    #-----------book-----end---------

