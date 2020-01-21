import re


ZK = "钻孔编号、勘探点类型、X坐标、Y坐标、偏移量、孔口标高、水面标高、勘探深度、探井深度、钻孔直径、勘探开始日期、勘探结束日期"
ZK_header = (1, 0)
TC = "岩土名称、层底深度、地层厚度、主层编号、亚层编号、次亚层编号、地质时代、地质成因、颜色、密实度、湿度、可塑性、浑圆度、均匀性、风化程度、岩层倾向、岩层倾角、矿物成分、结构构造、包含物、气味、描述、完整程度、坚硬程度、破碎程度、节理发育、节理间距"
TC_header = (1, 4)
BG = "试验点的底深度(m)、标贯类型、特征值、杆长(m)、一阵击数的长度(m)、一阵击数、标贯击数、标贯修正系数（中间结果）、修正后的标贯击数、修正否、参与否"
BG_header = (1, 1)
DT = "试验点的底深度(m)、动探类型(1-轻型/2-重型/3-超重型)、杆长(m)、试验段长度(m)、一阵击数、贯入度、动探击数、修正后击数、修正否、参与否"
DT_header = (1, 1)
SW = "水位深度(m)、地下水类型(0-初见水位 1-稳定水位)、地下水位层号、测水日期、地下水温、水位范围、地下水性质(1-上层滞水/2-潜水/3-承压水/4-其它)、参与否"
SW_header = (1, 1)

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


def get_ZK_header():
    return ZK_header


def get_TC_dict():
    TC_dict = to_dict(TC)
    return TC_dict


def get_TC_header():
    return TC_header


def get_BG_dict():
    BG_dict = to_dict(BG)
    return BG_dict


def get_BG_header():
    return BG_header


def get_DT_dict():
    DT_dict = to_dict(DT)
    return DT_dict


def get_DT_header():
    return DT_header


def get_SW_dict():
    SW_dict = to_dict(SW)
    return SW_dict


def get_SW_header():
    return SW_header
