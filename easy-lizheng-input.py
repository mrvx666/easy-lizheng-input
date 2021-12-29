# -*- coding: utf-8 -*-

"""
Author:mrvx666
Website:https://github.com/mrvx666/easy-lizheng-input
Info:这是ESI的主窗体，这个文件主要负责用户界面的输入输出。
"""

import os
from utils.excel import result
import sys
from time import sleep


def get_filename():
    filename = ""

    arglist = len(sys.argv)
    if arglist == 2:
        filename = sys.argv[1]
    elif arglist == 1:
        print("\n")
        path = os.getcwd()
        file_arr = []
        for dirpath, dirnames, files in os.walk(path):
            for file in files:
                if file.endswith(".xlsx"):
                    file_arr.append(file)
        print("检测到当前目录下存在文件：")

        for index, file in enumerate(file_arr):
            print(str(index+1) + "." + file)

        filename = ""
        index = input("请输入需要转换的文件序号，按下回车键继续\n")
        try:
            filename = file_arr[int(index) - 1]
            print("转换文件名为： " + filename)
        except:
            print("输入文件序号错误或未输入文件序号，文件序号需为正整数")

    elif arglist > 2:
        print('提示：只允许拖入单个文件')
    return filename


def main():
    filename = get_filename()
    try:
        output_file_name = result(filename)
        return output_file_name

    except FileNotFoundError:
        print("文件不存在，请检查文件是否存在当前目录下")


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

        input("程序运行异常...按下任意键退出")

