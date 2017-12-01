#coding=utf-8

#处理数据类型language
import os

lang_indent = "\t" #语言包的缩进
lang_pkg_dir = "lang_pkg/"
idx_col = 1  #语言包的idx所在列
cont_col = 2 #语言包内容所在列
data_begin_row = 1 #语言包数据开始的行

def handle_lang_package(lang_sheet_, output_path_):
    pass
    dir_name = output_path_ + lang_pkg_dir
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    lang_pkg_file_name = dir_name + lang_sheet_.cell_value(0, 1)
    lang_pkg_table_name = lang_sheet_.cell_value(0, 2)
    total_rows = lang_sheet_.nrows
    data_names = lang_sheet_.col_values(idx_col)
    data_vals = lang_sheet_.col_values(cont_col)
    lang_content = "%s={\n" % lang_pkg_table_name
    for x in range(data_begin_row, total_rows):
        pass
        data_str = handle_one_lang(data_names[x], data_vals[x])
        lang_content = lang_content + data_str

    lang_content = lang_content + "}"

    lang_file = open(lang_pkg_file_name, "w")
    lang_file.write(lang_content)
    lang_file.close()

#返回一行lang
def handle_one_lang(data_name_, data_val_):
    pass
    # data_str = "%s%s = \"%s\",\n" % (lang_indent, data_name_, data_val_)
    data_str = lang_indent + str(data_name_) + " = \"%s\"" % data_val_ + ",\n"
    return data_str
