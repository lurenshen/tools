#coding=utf-8

data_begin_row = 4
data_begin_col = 2
def cal_need_total_rows(sheet_, row_index_):
    pass
    temp_list = []
    total_rows = sheet_.nrows
    for x in range(data_begin_row, total_rows):
        pass
        data_row = sheet_.row_values(x)
        if row_index_ == data_row[data_begin_col-1]:
            temp_list.append(x)

    return len(temp_list)

def cal_need_total_cols(data_row_, total_cols):
    pass
    temp_list = []
    for x in range(data_begin_col, total_cols):
        pass
        if data_row_[x] != "":
            temp_list.append(x)

    return len(temp_list)
