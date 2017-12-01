# coding=utf-8

import os.path
import os
import sys
import xlrd
import shutil
import codecs

import global_var as gvar
import global_func as gfunc

import handle_book

#
gvar._init()
# gvar.set_value('name', 'cc')
# name = gvar.get_value('name')

#
def main(argv):
	#python main.py excel json
	print("main() %s" % argv)

	input_dir = "excel"
	output_dir = "json"
	postfix = "json"

	argc = len(argv)
	if argc >= 3:
		input_dir = argv[1]
		output_dir = argv[2]
		postfix = argv[3]

	#删除输出目录
	if os.path.exists(output_dir):
		__import__('shutil').rmtree(output_dir)

	#创建输出目录
	os.makedirs(output_dir)

	#遍历文件夹中的所有文件
	input_dir_list = os.listdir(input_dir)
	for x in range(len(input_dir_list)):
		path = "%s/%s" % (input_dir, input_dir_list[x])
		print("%s ... " % path)
		#
		workbook = xlrd.open_workbook(path)
		handle_book.handle_workbook(workbook, output_dir, postfix)
		print("%s ... ok " % path)
#
if __name__=="__main__":
	main(sys.argv)
