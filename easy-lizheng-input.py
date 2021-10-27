# -*- coding: utf-8 -*-

"""
Author:mrvx666
Website:https://github.com/mrvx666/easy-lizheng-input
Info:这是ESI的主窗体，主要的业务都在这里完成。
"""

from ZK import zk_read
from TC import tc_read
from BG import bg_read
from DT import dt_read
from SW import sw_read
from QY import qy_read
from excel import read_rawdata
from config import get_list, ZK_list, TC_list, BG_list, DT_list, SW_list, QY_list
import codecs
import datetime
import sys
from time import sleep


def get_last_key(data):
    datalist = get_list(data)
    lastkey = datalist[-1]
    return lastkey


def data_temp_output(zk_name, datalist, endkey):
    output = ""

    if len(datalist) == 0:  # 如果某一个点没有标贯\动探\水位……数据块，跳过
        pass
    else:
        header = ""
        datalisttype = list(datalist[0].keys())[1]  # 根据传入的数据字典列表获取数据类型

        if datalisttype == "标贯数据":
            header = "#BG#"
        if datalisttype == "动探数据":
            header = "#DT#"
        if datalisttype == "水位数据":
            header = "#SW#"
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
        if tc_temp['钻孔编号'] == zk_name:  # 查找钻孔编号符合的数据
            for tc_temp_dict in tc_temp['土层数据']:  # 提取土层数据

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
                    tc_output = tc_output + data_output(header, tc_temp_dict, get_last_key(TC_list))
                    return tc_output
    # 返回一个空字符串，防止产生None
    return ""


def write_txt(zk_datalist, tc_datalist, bg_datalist, dt_datalist, sw_datalist, qy_datalist, filename):

    time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file_name = filename + "接口导出" + str(time) + ".txt"

    try:
        file = codecs.open(str(output_file_name), "w", "gbk")
        for ZK_data in zk_datalist:
            zk_name = ZK_data['钻孔编号']  # 获取钻孔编号

            try:
                # ---勘探点表写入---
                file.write(data_output("#ZK#", ZK_data, get_last_key(ZK_list), False) + "\r\n")
            except Exception as e:
                print("勘探点表写入失败\n" + str(e))

            try:
                # ---土层数据表写入---
                file.write(tc_temp_output("#TC#", zk_name, tc_datalist))
            except Exception as e:
                print("土层数据表写入失败\n" + str(e))

            try:
                # ---标贯数据表写入---
                # print(bg_datalist)
                out = data_temp_output(zk_name, bg_datalist, get_last_key(BG_list))
                file.write(out)
            except Exception as e:
                print("标贯数据表写入失败\n" + str(e))

            try:
                # ---动探数据表写入---
                file.write(data_temp_output(zk_name, dt_datalist, get_last_key(DT_list)))
            except Exception as e:
                print("动探数据表写入失败\n" + str(e))

            try:
                # ---水位数据表写入---
                file.write(data_temp_output(zk_name, sw_datalist, get_last_key(SW_list)))
            except Exception as e:
                print("水位数据表写入失败\n" + str(e))

            try:
                # --取样数据表写入---
                file.write(data_temp_output(zk_name, qy_datalist, get_last_key(QY_list)))
            except Exception as e:
                print("取样数据表写入失败\n" + str(e))
        file.close()
        return output_file_name

    except Exception as e:
        print("文件写入失败\n" + str(e))
        return -1


def get_filename():
    filename = ""

    l = len(sys.argv)
    if l == 2:
        filename = sys.argv[1]
    elif l == 1:
        filename = input("要转换的文件默认为“理正勘察标准数据接口模板”，按下回车继续\n" +
                         "如果要转换别的文件，请输入要转换的文件名（忽略.xlsx拓展名）\n" +
                         "要转换的文件应放在与本程序相同的目录下\n")
        if filename == "":
            filename = "理正勘察标准数据接口模板"
        filename += ".xlsx"
    elif l > 2:
        print('提示：只允许拖入单个文件')

    return filename


def main():
    filename = get_filename()
    try:
        zk, tc, bg, dt, sw, qy = read_rawdata(filename)
        zk_data = zk_read(zk)
        tc_data = tc_read(tc)
        bg_data = bg_read(bg)
        dt_data = dt_read(dt)
        sw_data = sw_read(sw)
        qy_data = qy_read(qy)
        output_file_name = write_txt(zk_data, tc_data, bg_data, dt_data, sw_data, qy_data, filename)
        return output_file_name

    except FileNotFoundError:
        print(filename + "文件不存在，请检查文件是否存在当前目录下")

if __name__ == '__main__':
    import traceback

    print("\n")
    print("*************************************************************")
    sleep(0.6)
    print("Author: mrvx666")
    sleep(0.5)
    print("Project website:https://github.com/mrvx666/easy-lizheng-input")
    sleep(0.4)
    print("*************************************************************")
    sleep(1)
    print("\n")

    try:
        output_file_name = main()

        print("转换完成，转换文件名为：\n" + output_file_name + "\n")

        print("***警告：导入到理正勘察前请务必备份理正数据库***\n")
        sleep(0.3)
        print("导入方法：①理正勘察8.5选择 接口→读入理正标准数据接口\n         ②理正勘察9.0选择 接口→读入旧版理正标准数据接口\n")
        sleep(0.3)
        input("按任意键退出...")

    except Exception:
        print("*************************************************************")
        print("错误信息 debug：")
        traceback.print_exc()
        print("*************************************************************")

        input("\n程序运行异常...按下任意键退出")

