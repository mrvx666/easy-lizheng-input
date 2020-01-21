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
import codecs
import datetime


def data_temp_output(file, zk_name, datalist, endkey):
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


def write_txt(zk_datalist, tc_datalist, bg_datalist, dt_datalist, sw_datalist, qy_datalist):

    time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file_name = "理正勘察标准数据接口导出" + str(time) + ".txt"
    file = codecs.open(output_file_name, "w", "gbk")
    for ZK_data in zk_datalist:
        zk_name = ZK_data['钻孔编号']  # 获取钻孔编号
        # ZK表写入开始
        file.write(";钻孔编号-" + zk_name + " 钻孔数据" + "\r\n")
        zk_output = data_output("#ZK#", ZK_data, "勘探结束日期", False)
        file.write(zk_output + "\r\n")
        # ZK表写入结束
        # TC表写入开始
        file.write(";钻孔编号-" + zk_name + " 土层数据" + "\r\n")
        tc_output = ""
        for tc_temp in tc_datalist:
            if tc_temp['钻孔编号'] == zk_name:  # 查找钻孔编号符合的数据
                for tc_temp_dict in tc_temp['分层数据']:  # 提取分层数据
                    if str(tc_temp_dict['层底深度']).strip() == "":  # 测试层底深度是否为空，防止数据错误
                        pass
                    else:
                        tc_output = tc_output + data_output("#TC#", tc_temp_dict, "节理间距")
        file.write(tc_output)
        # TC表写入结束
        # BG表写入开始
        data_temp_output(file, zk_name, bg_datalist, "参与否")
        # BG表写入结束
        # DT表写入开始
        data_temp_output(file, zk_name, dt_datalist, "参与否")
        # DT表写入结束
        # SW表写入开始
        data_temp_output(file, zk_name, sw_datalist, "参与否")
        # SW表写入结束
        # QY表写入开始
        data_temp_output(file, zk_name, qy_datalist, "回弹模量")
        # QY表写入结束

    file.close()


ZK, TC, BG, DT, SW, QY = read_rawdata("理正勘察标准数据接口模板.xlsx")
zk_data = zk_read(ZK)
tc_data = tc_read(TC)
bg_data = bg_read(BG)
dt_data = dt_read(DT)
sw_data = sw_read(SW)
qy_data = qy_read(QY)
write_txt(zk_data, tc_data, bg_data, dt_data, sw_data, qy_data)

