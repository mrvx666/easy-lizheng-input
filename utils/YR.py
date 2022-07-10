# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header, YR_CQL_CYF
import random


YR_dict = get_dict("岩石采取率")
YR_header_row, YR_header_col = get_header("岩石采取率")


def yr_read(sheet):

    outputarr = []
    zk_name = {}
    for row in range(sheet.nrows)[YR_header_row:]:  # [1:]是用来跳过第一行的,这行通常是表头
        temp = YR_dict.copy()  # 拷贝原始字典

        # 预设值，来自config.py，如果表格内写入数据，预设数据会被覆盖
        temp.update({'采取率参与否': YR_CQL_CYF})

        for col in range(sheet.ncols)[YR_header_col:]:
            key = sheet.cell_value(rowx=0, colx=col)

            data = sheet.cell_value(rowx=row, colx=col)

            if data == "":
                # 跳过孔号不处理
                pass
            else:
                # 对岩心采取率（%）或者RQD（%）进行取整
                if key == "岩心采取率（%）" or key == "RQD（%）":
                    print("data = " + str(data))
                    data = int(float(data))

                temp[key] = data

            if str(sheet.cell_value(rowx=row, colx=0)).strip() != "":
                zk_name = sheet.cell_value(rowx=row, colx=0)
            else:
                pass

            outputdict = {"钻孔编号": zk_name,
                          "岩石采取率": temp}

        outputarr.append(outputdict)
    return outputarr


# TODO:按要求生产指定采取率
def yr_random_RQD():
    pass


# TODO:从模板文件读取生成采取率要求
def yr_random_RQD_read(sheet):
    for row in range(sheet.nrows)[YR_header_row:]:
        pass