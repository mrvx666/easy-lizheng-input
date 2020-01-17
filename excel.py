# -*- coding: UTF-8 -*-
import xlrd

def read_rawdata(file):
    print('open excel success!')
    workbook = xlrd.open_workbook(file)
    sheet_ZK = workbook.sheet_by_name('勘探点表')
    sheet_TC = workbook.sheet_by_name('基本数据')
    sheet_BG = workbook.sheet_by_name('标贯')
    sheet_DT = workbook.sheet_by_name('动探')
    sheet_SW = workbook.sheet_by_name('水位')
    return (sheet_ZK,
            sheet_TC,
            sheet_BG,
            sheet_DT,
            sheet_SW)

ZK = read_rawdata("理正勘察标准数据接口模板.xlsx")[0]
print(ZK.name,ZK.nrows,ZK.ncols)


output_arr = []
itercars = iter(range(ZK.nrows))
next(itercars)  # 跳过第一行
for row in itercars:
    rowdata = ZK.row_values(row)
    output = "#ZK#"
    for data in rowdata[1:]:
        if data is not "":
            output = output + str(data) + "\t"
    output_arr.append(output)

print(output_arr)
print(output_arr[0])

