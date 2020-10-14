import re

ZK = "基本数据"
ZK_list = "钻孔编号、勘探点类型、X坐标、Y坐标、偏移量、孔口标高、水面标高、勘探深度、探井深度、钻孔直径、勘探开始日期、勘探结束日期"
ZK_header = (1, 0)

TC = "土层数据"
TC_list = "岩土名称、层底深度、地层厚度、主层编号、亚层编号、次亚层编号、地质时代、地质成因、颜色、密实度、湿度、可塑性、浑圆度、均匀性、风化程度、" \
     "岩层倾向、岩层倾角、矿物成分、结构构造、包含物、气味、描述、完整程度、坚硬程度、破碎程度、节理发育、节理间距"
TC_header = (1, 4)

BG = "标贯数据"
BG_list = "试验点的底深度(m)、标贯类型、特征值、杆长(m)、一阵击数的长度(m)、一阵击数、标贯击数、标贯修正系数（中间结果）、修正后的标贯击数、修正否、参与否"
BG_header = (1, 1)
# 标贯数据：特征值
BG_TZZ = 0
# 标贯数据：一阵击数的长度(m)
BG_YZJSCD = 0.3
# 标贯数据：参与否
BG_CYF = 1

DT = "动探数据"
DT_list = "试验点的底深度(m)、动探类型(1-轻型/2-重型/3-超重型)、杆长(m)、试验段长度(m)、一阵击数、贯入度、动探击数、修正后击数、修正否、参与否"
DT_header = (1, 1)
# 动探数据：动探类型
DT_DTLX = 2
# 动探数据：参与否
DT_CYF = 1

SW = "水位数据"
SW_list = "水位深度(m)、地下水类型(0-初见水位 1-稳定水位)、地下水位层号、测水日期、地下水温、水位范围、地下水性质(1-上层滞水/2-潜水/3-承压水/4-其它)、参与否"
SW_header = (1, 1)
# 水位数据：地下水类型(0-初见水位 1-稳定水位)
SW_DXSLX = 1
# 水位数据：地下水位层号
SW_DXSWCH = 1
# 水位数据：地下水性质(1-上层滞水/2-潜水/3-承压水/4-其它)
SW_DXSXZ = 2

QY = "取样数据"
QY_list = "取样编号、取样深度、取样长度、取样类型(0-原状土样，1-扰动土样，2-岩样，3-水样）、质量密度、土粒比重、含水量、液限、塑限、" \
     "最小密度、最大密度、水上休止角、水下休止角、渗透系数、水平渗透系数、垂直渗透系数、单轴抗压强度、自然抗压强度、饱和抗压强度、" \
     "抗拉强度、抗剪强度、软化系数、桩侧摩阻力、桩端摩阻力、十字板剪切强度、无侧限抗压强度（原状）、无侧限抗压强度（重塑）、灵敏度、" \
     "透水率、剪切波速、纵波波速、动弹性模量、动剪切模量、动泊松比、回弹模量"
QY_header = (1, 1)


def get_list(datastr):
    templist = re.split("、", datastr)
    return templist


def get_last_key(data):
    datalist = get_list(data)
    lastkey = datalist[-1]
    return lastkey


def to_dict(datalist):
    templist1 = get_list(datalist)
    templist2 = []
    for i in range(len(templist1)):
        templist2.append("")
    data_dict = dict(zip(templist1, templist2))
    return data_dict


def get_ZK_dict():
    ZK_dict = to_dict(ZK_list)
    return ZK_dict


def get_ZK_header():
    return ZK_header


def get_TC_dict():
    TC_dict = to_dict(TC_list)
    return TC_dict


def get_TC_header():
    return TC_header


def get_BG_dict():
    BG_dict = to_dict(BG_list)
    return BG_dict


def get_BG_header():
    return BG_header


def get_DT_dict():
    DT_dict = to_dict(DT_list)
    return DT_dict


def get_DT_header():
    return DT_header


def get_SW_dict():
    SW_dict = to_dict(SW_list)
    return SW_dict


def get_SW_header():
    return SW_header

def get_QY_dict():
    QY_dict = to_dict(QY_list)
    return QY_dict


def get_QY_header():
    return QY_header