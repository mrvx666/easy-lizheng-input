# -*- coding: UTF-8 -*-
import xlrd

def read_rawdata(file):
    workbook = xlrd.open_workbook(file)
    sheet_ZK = workbook.sheet_by_name('勘探点表')
    sheet_TC = workbook.sheet_by_name('土层数据')
    sheet_BG = workbook.sheet_by_name('标贯数据')
    sheet_DT = workbook.sheet_by_name('动探数据')
    sheet_SW = workbook.sheet_by_name('水位数据')
    sheet_QY = workbook.sheet_by_name('取样数据')
    return (sheet_ZK,
            sheet_TC,
            sheet_BG,
            sheet_DT,
            sheet_SW,
            sheet_QY)


def read_standard_formation(file):
    workbook = xlrd.open_workbook(file)
    sheet_BZDC = workbook.sheet_names('标准地层')
    return sheet_BZDC