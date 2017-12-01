#coding=utf-8

import xlrd
import os

'''
用于测试xlrd.sheet.Cell对象常用的一些方法
'''

'''
The following table describes the types of cells and how their values are represented in Python.

 Type-symbol   Type-number      Python-value
XL_CELL_EMPTY       0              empty string u''
XL_CELL_TEXT        1              a Unicode string
XL_CELL_NUMBER      2              float
XL_CELL_DATE        3              float
XL_CELL_BOOLEAN     4              int; 1 means TRUE, 0 means FALSE
XL_CELL_ERROR       5              int representing internal Excel codes; for a text representation, refer to the supplied dictionary error_text_from_code
XL_CELL_BLANK       6              empty string u''. Note: this type will appear only when open_workbook(..., formatting_info=True) is used.

'''

#xlrd and Book
# book_xlrd = xlrd.open_workbook(".\input\singleTab.xls")
# 如果文件名中包含中文，则需要进行转码，不然读取失败,文件名开头如果有数字，需要使用转义字符'\'
filename = ".\input\\001.xls"
# filename = filename.decode('utf-8')
book_xlrd = xlrd.open_workbook(filename)

#----------cell-------begin--------
#如果使用中文，确保使用前后的编码一致,如下的两个地方多要unicode一下
sheet_name = "主表"
sheet_name = sheet_name.decode("utf-8")
try:
    sheet = book_xlrd.sheet_by_name(sheet_name)
    cell = sheet.cell(0, 0)
except IndexError:
    print "cell index error"
except:
    print "there is no sheet '%s'" % sheet_name
else:
  print cell
  #cell.value
  print cell.value
  if cell.value == unicode('文件名/Table/子文件夹/是否带ID/添加子ID及大括号{}/去掉文件头',"utf-8"):
      print "hello world"
  #cell.ctype
  print cell.ctype
  #cell.xf_index
  print cell.xf_index
#----------cell-------end--------datemode
