# -*- coding: UTF-8 -*-
import xlrd

def read_rawdata(file):
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


def read_standard_formation(file):
    workbook = xlrd.open_workbook(file)
    sheet_BZDC = workbook.sheet_names('标准地层')
    return sheet_BZDC