# -*- coding: UTF-8 -*-
from config import get_QY_dict, get_QY_header


QY_dict = get_QY_dict()
QY_header_row, QY_header_col = get_QY_header()

def qy_read(sheet):
    outputarr = []
    for row in range(sheet.nrows)[QY_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = QY_dict.copy()  # 拷贝原始字典
        for col in range(sheet.ncols)[QY_header_col:]:
            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)
            if str(sheet.cell_value(rowx=row, colx=0)).strip() != "":
                zk_name = sheet.cell_value(rowx=row, colx=0)
            else:
                pass
            outputdict = {"钻孔编号": zk_name,
                          "取样数据": temp}

        outputarr.append(outputdict)

    return outputarr