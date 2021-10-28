# -*- coding: UTF-8 -*-
from utils.config import get_dict, get_header


TC_dict = get_dict("土层数据")
TC_header_row, TC_header_col = get_header("土层数据")


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

            # 从excel出来的层号可能是float类型，进行转换到整数，如果没有层号就跳过不处理
            try:
                tempdict['主层编号'] = int(tempdict['主层编号'])
                tempdict['亚层编号'] = int(tempdict['亚层编号'])
                tempdict['亚层编号'] = int(tempdict['次亚层编号'])
            except Exception as e:
                # print("层号不存在\n" + str(e))
                pass

            temparr.append(tempdict)
        zk_name = sheet.cell_value(rowx=0, colx=col)
        outputdict = {"钻孔编号": zk_name,
                     "土层数据": temparr}
        outputarr.append(outputdict)

    return outputarr



