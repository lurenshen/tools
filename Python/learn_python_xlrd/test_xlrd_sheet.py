#coding=utf-8

import xlrd
import os

'''
用于测试xlrd.sheet.Sheet对象常用的一些方法
'''

#xlrd and Book
# book_xlrd = xlrd.open_workbook(".\input\singleTab.xls")
# 如果文件名中包含中文，则需要进行转码，不然读取失败,文件名开头如果有数字，需要使用转义字符'\'
filename = ".\input\\001.xls"
# filename = filename.decode('utf-8')
book_xlrd = xlrd.open_workbook(filename)
print book_xlrd

#-----------sheet-----begin---------
#如果使用中文，确保使用前后的编码一致,如下的两个地方多要unicode一下
sheet_name = "主表"
sheet_name = sheet_name.decode("utf-8")
try:
    sheet = book_xlrd.sheet_by_name(sheet_name)
except:
    print "there is no sheet '%s'" % sheet_name
else:
    #col(colx) Returns a sequence of the Cell objects in the given column.
    print sheet.col(0)
    #book = None   A reference to the Book object to which this sheet belongs.
    print sheet.book
    #name = ''   Name of sheet.
    if sheet.name == unicode("主表","utf-8"): #和中文字符串比较，需要unicode
        print sheet.name #"主表"
    #sheet.nrows  Number of rows in sheet. A row index is in range(thesheet.nrows).
    print sheet.nrows
    #sheet.ncols
    print sheet.ncols
    #cell(rowx, colx)  Cell object in the given row and column.
    print sheet.cell(0, 0)
    #cell_value(rowx, colx)  Value of the cell in the given row and column.
    print sheet.cell_value(0, 0)
    #cell_type(rowx, colx)  Type of the cell in the given row and column. Refer to the documentation of the Cell class.
    print sheet.cell_type(0, 0)
    #row_len(rowx)  Returns the effective number of cells in the given row. For use with open_workbook(ragged_rows=True) which is likely to produce rows with fewer than ncols cells.
    print sheet.row_len(0)
    #row(rowx)  Returns a sequence of the Cell objects in the given row.
    print sheet.row(0)
    #row_types(rowx, start_colx=0, end_colx=None) Returns a slice of the types of the cells in the given row.
    print sheet.row_types(0)
    #row_values(rowx, start_colx=0, end_colx=None) Returns a slice of the values of the cells in the given row.
    print sheet.row_values(0)
    #row_slice(rowx, start_colx=0, end_colx=None)   Returns a slice of the Cell objects in the given row.
    print sheet.row_slice(0) #和row(rowx)相等
    #col_slice(colx, start_rowx=0, end_rowx=None)   Returns a slice of the Cell objects in the given column.
    print sheet.col_slice(0) #equal to col(colx)
    #col_values(colx, start_rowx=0, end_rowx=None)  Returns a slice of the values of the cells in the given column.
    print sheet.col_values(0)
    #col_types(colx, start_rowx=0, end_rowx=None)   Returns a slice of the types of the cells in the given column.
    print sheet.col_types(0)
#-----------sheet-----end---------

