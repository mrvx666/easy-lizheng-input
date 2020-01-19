# -*- coding: UTF-8 -*-
from config import get_TC_dict, get_TC_header


TC_dict = get_TC_dict()
TC_header_row, TC_header_col = get_TC_header()


def tc_read(sheet):
    outputarr = []
    for col in range(sheet.ncols)[TC_header_col:]:
        temparr = []

        for row in range(sheet.nrows)[TC_header_row:]:  # 跳过钻孔编号
            tempdict = TC_dict.copy()  # 拷贝原始字典
            for colX in range(TC_header_col):  # 用于确定表头
                if colX >= TC_header_col-1:
                    key = "层底深度"
                    tempdict[key] = sheet.cell_value(rowx=row, colx=col)
                else:
                    key = sheet.cell_value(rowx=0, colx=colX)
                    tempdict[key] = sheet.cell_value(rowx=row, colx=colX)
            temparr.append(tempdict)
        zk_name = sheet.cell_value(rowx=0, colx=col)
        outputdict = {"钻孔编号": zk_name,
                     "分层数据": temparr}
        outputarr.append(outputdict)

    return outputarr



