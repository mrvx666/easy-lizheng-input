# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header, QY_QYCD


QY_dict = get_dict("取样数据")
QY_header_row, QY_header_col = get_header("取样数据")

def qy_read(sheet):
    outputarr = []
    for row in range(sheet.nrows)[QY_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = QY_dict.copy()  # 拷贝原始字典

        for col in range(sheet.ncols)[QY_header_col:]:
            if str(sheet.cell_value(rowx=row, colx=0)).strip() != "":  # 检测第一列数据作为钻孔编号
                zk_name = str(sheet.cell_value(rowx=row, colx=0))
                count = 1  # 用于取样编号

            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)
            outputdict = {"钻孔编号": zk_name,
                          "取样数据": temp}
        temp.update({'取样编号': count})
        temp.update({'取样长度': QY_QYCD})
        count += 1
        outputarr.append(outputdict)

    return outputarr