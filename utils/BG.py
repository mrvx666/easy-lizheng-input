# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header, BG_TZZ, BG_YZJSCD, BG_CYF


BG_dict = get_dict("标贯数据")
BG_header_row, BG_header_col = get_header("标贯数据")


def bg_read(sheet):
    outputarr = []
    zk_name = {}
    for row in range(sheet.nrows)[BG_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = BG_dict.copy()  # 拷贝原始字典

        # 预设值，来自config.py，如果表格内写入数据，预设数据会被覆盖
        temp.update({'特征值': BG_TZZ})
        temp.update({'一阵击数的长度(m)': BG_YZJSCD})
        temp.update({'参与否': BG_CYF})

        for col in range(sheet.ncols)[BG_header_col:]:
            key = sheet.cell_value(rowx=0, colx=col)

            # 对标贯动探击数进行取整
            if key == "标贯击数" or key == "参与否":
                temp[key] = int(sheet.cell_value(rowx=row, colx=col))
            else:
                temp[key] = sheet.cell_value(rowx=row, colx=col)

            if str(sheet.cell_value(rowx=row, colx=0)).strip() != "":
                zk_name = sheet.cell_value(rowx=row, colx=0)
            else:
                pass

            outputdict = {"钻孔编号": zk_name,
                          "标贯数据": temp}

        outputarr.append(outputdict)
    return outputarr

