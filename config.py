import re


ZK = "钻孔编号、勘探点类型、X坐标、Y坐标、偏移量、孔口标高、水面标高、勘探深度、探井深度、钻孔直径、勘探开始日期、勘探结束日期"
ZK_header = ()
TC = "岩土名称、层底深度、地层厚度、主层编号、亚层编号、次亚层编号、地质时代、地质成因、颜色、密实度、湿度、可塑性、浑圆度、均匀性、风化程度、岩层倾向、岩层倾角、矿物成分、结构构造、包含物、气味、描述、完整程度、坚硬程度、破碎程度、节理发育、节理间距"
TC_header = (1, 4)


def to_dict(datalist):
    templist1 = re.split("、", datalist)
    templist2 = []
    for i in range(len(templist1)):
        templist2.append("")
    data_dict = dict(zip(templist1, templist2))
    return data_dict


def get_ZK_dict():
    ZK_dict = to_dict(ZK)
    return ZK_dict


def get_TC_dict():
    TC_dict = to_dict(TC)
    return TC_dict

def get_TC_header():
    return TC_header
