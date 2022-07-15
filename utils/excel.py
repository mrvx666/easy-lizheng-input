"""
Author:mrvx666
Website:https://github.com/mrvx666/easy-lizheng-input
Info:这个文件主要负责操作读写数据。
"""

import xlrd
import codecs
from utils.config import get_last_key
from utils.ZK import zk_read
from utils.TC import tc_read
from utils.BG import bg_read
from utils.DT import dt_read
from utils.SW import sw_read
from utils.YR import yr_read
from utils.QY import qy_read
from time import strftime


def timeFileName(filename):
    time = strftime("%Y-%m-%d-%H-%M-%S")
    return filename + "接口导出" + str(time) + ".txt"


def data_temp_output(zk_name, datalist, endkey):
    output = ""

    if len(datalist) == 0:  # 如果某一个点没有标贯\动探\水位……数据块，跳过
        pass
    else:
        datalisttype = list(datalist[0].keys())[1]  # 根据传入的数据字典列表获取数据类型
        if datalisttype == "基本数据":
            header = "#ZK#"
        if datalisttype == "土层数据":
            header = "#TC#"
        if datalisttype == "标贯数据":
            header = "#BG#"
        if datalisttype == "动探数据":
            header = "#DT#"
        if datalisttype == "水位数据":
            header = "#SW#"
        if datalisttype == "岩石采取率":
            header = "#YR#"
        if datalisttype == "取样数据":
            header = "#QY#"
        for temp in datalist:
            if temp['钻孔编号'] == zk_name:  # 查找钻孔编号符合的数据
                output = output + data_output(header, temp[datalisttype], endkey)

    # 返回一个空字符串，防止产生None
    return output


def data_output(header, data_dict, endkey, line_feed=True):
    output = header
    for key in data_dict:
        # 如果单元格为空，跳过不做处理
        if str(data_dict[key]).strip() == "":
            pass
        else:
            output = output + str(data_dict[key])

        if key == endkey:
            pass
        else:
            output = output + "\t"

    if line_feed:
        output = output + "\r\n"
    return output


def tc_temp_output(header, zk_name, tc_datalist):
    tc_output = ""
    for tc_temp in tc_datalist:
        print(tc_temp)
        if tc_temp['钻孔编号'] == zk_name:  # 查找钻孔编号符合的数据
            for tc_temp_dict in tc_temp['土层数据']:  # 提取土层数据
                print(tc_temp_dict)
                # 如果从excel读取出来是str类型，大概率是空格，判断是否为空
                if isinstance(tc_temp_dict['层底深度'], str):
                    if str(tc_temp_dict['主层编号']).strip() == "":
                        # excel中有空格可能会被识别为有数据，判断主层编号为空则跳过不做处理
                        pass
                    else:
                        # 数据效验，提示用户部分地层不连续
                        print(zk_name + " 第" + str(tc_temp_dict['主层编号']) + " - " +
                              str(tc_temp_dict['亚层编号']) + " - " +str(tc_temp_dict['次亚层编号'])
                              + "层 层底深度为空")

                elif tc_temp_dict['岩土名称'].strip() == "":
                    print(zk_name + " 存在岩土名称为空的空行")

                else:
                    tc_output = tc_output + data_output(header, tc_temp_dict, get_last_key("土层数据"))
                    return tc_output
    # 返回一个空字符串，防止产生None
    return ""


def write_txt(zk_datalist, tc_datalist, bg_datalist, dt_datalist, sw_datalist, yr_datalist, qy_datalist, out_file_name):
    try:
        file = codecs.open(str(out_file_name), "w", "gbk")
        for ZK_data in zk_datalist:
            zk_name = ZK_data['钻孔编号']  # 获取钻孔编号

            try:
                # ---勘探点表写入---
                out = data_output("#ZK#", ZK_data, get_last_key("基本数据"), False) + "\r\n"
                file.write(out)
            except Exception as e:
                print("勘探点表写入失败\n" + str(e))

            # try:
            #     # ---土层数据表写入---
            #     out = tc_temp_output("#TC#", zk_name, tc_datalist)
            #     file.write(out)
            # except Exception as e:
            #     print("土层数据表写入失败\n" + str(e))

            try:
                # ---标贯数据表写入---
                out = data_temp_output(zk_name, bg_datalist, get_last_key("标贯数据"))
                file.write(out)
            except Exception as e:
                print("标贯数据表写入失败\n" + str(e))

            try:
                # ---动探数据表写入---
                file.write(data_temp_output(zk_name, dt_datalist, get_last_key("动探数据")))
            except Exception as e:
                print("动探数据表写入失败\n" + str(e))

            try:
                # ---水位数据表写入---
                file.write(data_temp_output(zk_name, sw_datalist, get_last_key("水位数据")))
            except Exception as e:
                print("水位数据表写入失败\n" + str(e))

            try:
                # --采取率数据表写入---
                file.write(data_temp_output(zk_name, yr_datalist, get_last_key("岩石采取率")))
            except Exception as e:
                print("采取率数据表写入失败\n" + str(e))

            try:
                # --取样数据表写入---
                file.write(data_temp_output(zk_name, qy_datalist, get_last_key("取样数据")))
            except Exception as e:
                print("取样数据表写入失败\n" + str(e))
        file.close()
        return out_file_name

    except Exception as e:
        print("文件写入失败\n" + str(e))
        return -1


def read_rawdata(file):
    workbook = xlrd.open_workbook(file)
    sheet_ZK = workbook.sheet_by_name('勘探点表')
    sheet_TC = workbook.sheet_by_name('土层数据')
    sheet_BG = workbook.sheet_by_name('标贯数据')
    sheet_DT = workbook.sheet_by_name('动探数据')
    sheet_SW = workbook.sheet_by_name('水位数据')
    sheet_YR = workbook.sheet_by_name('岩石采取率')
    sheet_QY = workbook.sheet_by_name('取样数据')
    return (sheet_ZK,
            sheet_TC,
            sheet_BG,
            sheet_DT,
            sheet_SW,
            sheet_YR,
            sheet_QY)


def result(filename):
    zk, tc, bg, dt, sw, yr, qy = read_rawdata(filename)
    zk_data = zk_read(zk)
    tc_data = tc_read(tc)
    bg_data = bg_read(bg)
    dt_data = dt_read(dt)
    sw_data = sw_read(sw)
    yr_data = yr_read(yr)
    qy_data = qy_read(qy)
    output_file_name = write_txt(zk_data, tc_data, bg_data, dt_data, sw_data, yr_data, qy_data, timeFileName(filename))
    print("info:转换完成，转换后接口文件为：\n" + output_file_name.split("\\")[-1] + "\n")


