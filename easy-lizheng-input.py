# -*- coding: utf-8 -*-

"""
Author:mrvx666
Website:https://github.com/mrvx666/easy-lizheng-input
Info:这是ESI的主窗体，这个文件主要负责用户界面的输入输出。
"""

from utils.excel import result
import sys
from time import sleep


def get_filename():
    filename = ""

    arglist = len(sys.argv)
    if arglist == 2:
        filename = sys.argv[1]
    elif arglist == 1:
        filename = input("要转换的文件默认为“理正勘察标准数据接口模板”，按下回车继续\n" +
                         "如果要转换别的文件，请输入要转换的文件名（忽略.xlsx拓展名）\n" +
                         "要转换的文件应放在与本程序相同的目录下\n")
        if filename == "":
            filename = "理正勘察标准数据接口模板"
        filename += ".xlsx"
        print("转换文件名为： " + filename)
    elif arglist > 2:
        print('提示：只允许拖入单个文件')
    return filename


def main():
    filename = get_filename()
    try:
        output_file_name = result(filename)
        return output_file_name

    except FileNotFoundError:
        print(filename + " 文件不存在，请检查文件是否存在当前目录下")


if __name__ == '__main__':
    import traceback

    print("\n")
    print("*************************************************************")
    sleep(0.6)
    print("Project: easy-lizheng-input")
    sleep(0.5)
    print("Author: mrvx666")
    sleep(0.5)
    print("Project website:https://github.com/mrvx666/easy-lizheng-input")
    sleep(0.4)
    print("Note：本程序提供excel文件转换为理正标准数据接口的功能")
    sleep(0.3)
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
        print("\n*************************************************************")
        print("错误信息 debug：")
        traceback.print_exc()
        print("*************************************************************")

        input("\n程序运行异常...按下任意键退出")

