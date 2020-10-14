# -*- coding: utf-8 -*-

"""
这是ESI的主窗体，主要的业务都在这里完成。
"""

from ZK import zk_read
from TC import tc_read
from BG import bg_read
from DT import dt_read
from SW import sw_read
from QY import qy_read
from excel import read_rawdata
from config import get_last_key, ZK_list, TC_list, BG_list, DT_list, SW_list, QY_list
import codecs
import datetime


def data_temp_output(file, zk_name, datalist, endkey):
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

        file.write(";钻孔编号-" + zk_name + " " + datalisttype + "\r\n")
        output = ""
        for temp in datalist:
            if temp['钻孔编号'] == zk_name:  # 查找钻孔编号符合的数据
                output = output + data_output(header, temp[datalisttype], endkey)
        file.write(output)


def data_output(header, dict, endkey, line_feed=True):
    output = header
    for key in dict:
        if str(dict[key]).strip() == "":
            pass
        else:
            output = output + str(dict[key])

        if key == endkey:
            pass
        else:
            output = output + "\t"

    if line_feed == True:
        output = output + "\r\n"
    return output


def write_txt(zk_datalist, tc_datalist, bg_datalist, dt_datalist, sw_datalist, qy_datalist, filename):

    time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file_name = filename + "接口导出" + str(time) + ".txt"

    try:
        file = codecs.open(str(output_file_name), "w", "gbk")
    except Exception as e:
        print("文件打开失败\n" + str(e))

    for ZK_data in zk_datalist:
        zk_name = ZK_data['钻孔编号']  # 获取钻孔编号

        try:
            # ---勘探点表写入---
            file.write(";钻孔编号-" + zk_name + " 钻孔数据" + "\r\n")
            zk_output = data_output("#ZK#", ZK_data, get_last_key(ZK_list), False)
            file.write(zk_output + "\r\n")
        except Exception as e:
            print("勘探点表写入失败\n" + str(e))

        try:
            # ---土层数据表写入---
            file.write(";钻孔编号-" + zk_name + " 地层数据" + "\r\n")
            tc_output = ""
            for tc_temp in tc_datalist:
                if tc_temp['钻孔编号'] == zk_name:  # 查找钻孔编号符合的数据
                    for tc_temp_dict in tc_temp['分层数据']:  # 提取分层数据
                        if str(tc_temp_dict['层底深度']).strip() == "":  # 测试层底深度是否为空，防止数据错误
                            pass
                        else:
                            tc_output = tc_output + data_output("#TC#", tc_temp_dict, get_last_key(TC_list))
            file.write(tc_output)
        except Exception as e:
            print("土层数据表写入失败\n" + str(e))

        try:
            # ---标贯数据表写入---
            data_temp_output(file, zk_name, bg_datalist, get_last_key(BG_list))
        except Exception as e:
            print("标贯数据表写入失败\n" + str(e))

        try:
            # ---动探数据表写入---
            data_temp_output(file, zk_name, dt_datalist, get_last_key(DT_list))
        except Exception as e:
            print("动探数据表写入失败\n" + str(e))

        try:
            # ---水位数据表写入---
            data_temp_output(file, zk_name, sw_datalist, get_last_key(SW_list))
        except Exception as e:
            print("水位数据表写入失败\n" + str(e))
        try:
            # --取样数据表写入---
            data_temp_output(file, zk_name, qy_datalist, get_last_key(QY_list))
        except Exception as e:
            print("取样数据表写入失败\n" + str(e))

    file.close()
    return output_file_name


filename = input("要转换的文件默认为“理正勘察标准数据接口模板”，按下回车继续\n"+"如果要转换别的文件，请输入要转换的文件名（忽略.xlsx拓展名）\n")
if filename == "":
    filename = "理正勘察标准数据接口模板"
filename += ".xlsx"

try:
    ZK, TC, BG, DT, SW, QY = read_rawdata(filename)
    zk_data = zk_read(ZK)
    tc_data = tc_read(TC)
    bg_data = bg_read(BG)
    dt_data = dt_read(DT)
    sw_data = sw_read(SW)
    qy_data = qy_read(QY)
    output_file_name = write_txt(zk_data, tc_data, bg_data, dt_data, sw_data, qy_data, filename)
    input("转换完成，文件名：" + output_file_name + "\n导入到理正前请务必备份原有的理正数据库" + "\n请按任意键退出.......")
except Exception as e:
    print("转换失败" + "\n请按任意键退出.......")
    input()
