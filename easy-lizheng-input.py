# -*- coding: utf-8 -*-

"""
这是ESI的主窗体，主要的业务都在这里完成。
"""

from ZK import zk_read
from TC import tc_read
from BG import bg_read
from DT import dt_read
from SW import sw_read
from excel import read_rawdata
import codecs
import datetime


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


def write_txt(ZK_datalist,TC_datalist,BG_datalist,DT_datalist,SW_datalist):
    count = 1
    time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file_name = "理正勘察标准数据接口导出" + str(time) + ".txt"
    file = codecs.open(output_file_name, "w", "gbk")
    for ZK_data in ZK_datalist:

        # ZK表写入开始
        file.write(";钻孔编号-" + ZK_data['钻孔编号'] + " 钻孔数据" + "\r\n")
        ZK_output = data_output("#ZK#", ZK_data, "勘探结束日期", False)
        file.write(ZK_output + "\r\n")
        # ZK表写入结束
        # TC表写入开始
        file.write(";钻孔编号-" + ZK_data['钻孔编号'] + " 土层数据" + "\r\n")
        TC_output = ""
        for tc_temp in TC_datalist:
            if tc_temp['钻孔编号'] == ZK_data['钻孔编号']:  # 查找钻孔编号符合的数据
                for tc_temp_dict in tc_temp['分层数据']:  # 提取分层数据
                    if str(tc_temp_dict['层底深度']).strip() == "":  # 测试层底深度是否为空，防止数据错误
                        pass
                    else:
                        TC_output = TC_output + data_output("#TC#", tc_temp_dict, "节理间距", True)
                file.write(TC_output)
        # TC表写入结束
        # BG表写入开始
        file.write(";钻孔编号-" + ZK_data['钻孔编号'] + " 标贯数据" + "\r\n")
        BG_output = ""
        for bg_temp in BG_datalist:
            if bg_temp['钻孔编号'] == ZK_data['钻孔编号']:  # 查找钻孔编号符合的数据
                BG_output = BG_output + data_output("#BG#", bg_temp['标贯数据'], "参与否", True)
        file.write(BG_output)
        # BG表写入结束
        # DT表写入开始
        file.write(";钻孔编号-" + ZK_data['钻孔编号'] + " 动探数据" + "\r\n")
        DT_output = ""
        for dt_temp in DT_datalist:
            if dt_temp['钻孔编号'] == ZK_data['钻孔编号']:  # 查找钻孔编号符合的数据
                DT_output = DT_output + data_output("#DT#", dt_temp['标贯数据'], "参与否", True)
        file.write(DT_output)
        # DT表写入结束
        # SW表写入开始
        file.write(";钻孔编号-" + ZK_data['钻孔编号'] + " 水位数据" + "\r\n")
        SW_output = ""
        for bg_temp in SW_datalist:
            if bg_temp['钻孔编号'] == ZK_data['钻孔编号']:  # 查找钻孔编号符合的数据
                SW_output = SW_output + data_output("#SW#", bg_temp['水位数据'], "参与否", True)
        file.write(SW_output)
        # SW表写入结束
        count = count + 1


    file.close()


ZK, TC, BG, DT, SW = read_rawdata("理正勘察标准数据接口模板.xlsx")
zk_data = zk_read(ZK)
tc_data = tc_read(TC)
bg_data = bg_read(BG)
dt_data = dt_read(DT)
sw_data = sw_read(SW)
write_txt(zk_data,tc_data,bg_data,dt_data,sw_data)