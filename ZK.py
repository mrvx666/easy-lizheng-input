# -*- coding: UTF-8 -*-
from config import get_ZK_dict
from excel import read_rawdata


ZK_dict = get_ZK_dict()


def zk_read(sheet):
    outputarr = []
    count = 0
    for row in range(sheet.nrows)[1:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = ZK_dict.copy()  # 拷贝原始字典
        for col in range(sheet.ncols):
            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)
            count = count + 1
        outputarr.append(temp)
    return outputarr


