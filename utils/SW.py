# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header, SW_DXSLX, SW_DXSWCH, SW_CYF


SW_dict = get_dict("水位数据")
SW_header_row, SW_header_col = get_header("水位数据")


def sw_read(sheet):
    outputarr = []
    for row in range(sheet.nrows)[SW_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = SW_dict.copy()  # 拷贝原始字典

        # 预设值，来自config.py，如果表格内写入数据，预设数据会被覆盖
        temp.update({'地下水类型(0-初见水位 1-稳定水位)': SW_DXSLX})
        temp.update({'地下水位层号': SW_DXSWCH})
        temp.update({'地下水性质(1-上层滞水/2-潜水/3-承压水/4-其它)': SW_DXSWCH})
        temp.update({'参与否': SW_CYF})

        for col in range(sheet.ncols)[SW_header_col:]:
            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)

        zk_name = sheet.cell_value(rowx=row, colx=0)
        outputdict = {"钻孔编号": zk_name,
                      "水位数据": temp}
        outputarr.append(outputdict)
    return outputarr





