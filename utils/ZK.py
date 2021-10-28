# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header


ZK_dict = get_dict("基本数据")
ZK_header_row, ZK_header_col = get_header("基本数据")


def zk_read(sheet):
    outputarr = []
    count = 0
    for row in range(sheet.nrows)[ZK_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = ZK_dict.copy()  # 拷贝原始字典
        for col in range(sheet.ncols):
            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)
            count = count + 1
        outputarr.append(temp)
    return outputarr


