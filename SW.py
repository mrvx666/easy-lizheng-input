# -*- coding: UTF-8 -*-
from config import get_SW_dict,get_SW_header
from excel import read_rawdata



SW_dict = get_SW_dict()
SW_header_row, SW_header_col = get_SW_header()


def sw_read(sheet):
    outputarr = []
    for row in range(sheet.nrows)[SW_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = SW_dict.copy()  # 拷贝原始字典
        for col in range(sheet.ncols)[SW_header_col:]:
            key = sheet.cell_value(rowx=0, colx=col)
            temp[key] = sheet.cell_value(rowx=row, colx=col)
        zk_name = sheet.cell_value(rowx=row, colx=0)
        outputdict = {"钻孔编号": zk_name,
                      "水位数据": temp}
        outputarr.append(outputdict)
    return outputarr


ZK,TC,BG,DT,SW = read_rawdata("理正勘察标准数据接口模板.xlsx")
sw_data = sw_read(SW)

