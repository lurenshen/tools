# coding=utf-8

import os.path
import handle_book
import os
import sys
import xlrd

def main():
	#遍历文件夹中的所有文件
	dirlist = os.listdir("./input")
	output_path = "./output/"
	for x in range(len(dirlist)):
		pass
		book = xlrd.open_workbook("./input/%s" % dirlist[x])
		handle_book.handle_workbook(book, output_path)

if __name__=="__main__":
	main()

