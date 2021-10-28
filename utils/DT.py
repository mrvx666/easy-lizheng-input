# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header, DT_DTLX, DT_CYF


DT_dict = get_dict("动探数据")
DT_header_row, DT_header_col = get_header("动探数据")


def dt_read(sheet):
    outputarr = []
    zk_name = {}
    for row in range(sheet.nrows)[DT_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = DT_dict.copy()  # 拷贝原始字典

        # 预设值，来自config.py，如果表格内写入数据，预设数据会被覆盖
        temp.update({'动探类型': DT_DTLX})
        temp.update({'参与否': DT_CYF})

        for col in range(sheet.ncols)[DT_header_col:]:
            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)
            if str(sheet.cell_value(rowx=row, colx=0)).strip() != "":
                zk_name = sheet.cell_value(rowx=row, colx=0)
            else:
                pass

            outputdict = {"钻孔编号": zk_name,
                          "动探数据": temp}

        outputarr.append(outputdict)
    return outputarr