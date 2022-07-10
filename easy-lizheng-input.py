# -*- coding: utf-8 -*-

"""
Author:mrvx666
Website:https://github.com/mrvx666/easy-lizheng-input
Info:这是ESI的主窗体，这个文件主要负责用户界面的输入输出。
"""

import sys
from os import getcwd, walk
from time import sleep

from utils.config import get_time
from utils.excel import result
from utils.YR import yr_random_RQD


def get_filename():
    filename = ""
    random_rqd = False

    arglist = len(sys.argv)
    if arglist == 2:
        filename = sys.argv[1]
    elif arglist == 1:
        print("\n")

        file_arr = print_file_list()

        if len(file_arr) == 0:
            print("error:当前目录下不存在模板接口文件（.xlsx），请检查工作目录")
            return 0
        else:
            print("info:检测到当前目录下存在文件：")

            fileindex = get_filename_index(file_arr)

            if fileindex.endswith("RQD"):
                random_rqd = True
            else:
                filename = file_arr[int(fileindex) - 1]

    elif arglist > 2:
        print('error:只允许拖入单个文件')

    if filename == "":
        print("info:输入文件序号错误或未输入文件序号，文件序号需为正整数\n")
        raise FileNotFoundError

    return filename, random_rqd


def print_file_list():
    path = getcwd()
    file_arr = []
    for dirpath, dirnames, files in walk(path):
        for file in files:
            if file.endswith(".xlsx"):
                file_arr.append(file)
    return file_arr


def get_filename_index(file_arr):
    for index, file in enumerate(file_arr):
        print(str(index + 1) + "." + file)

    index = input("\ninfo:请输入需要转换的文件序号，按下回车键继续\n")
    print(index)
    return index


def main():

    print("\n")
    print("*************************************************************")
    sleep(0.6)
    print("Project: easy-lizheng-input")
    sleep(0.5)
    print("Author: mrvx666            QQ：377873597")
    sleep(0.5)
    print("Project website:https://github.com/mrvx666/easy-lizheng-input")
    sleep(0.4)
    print("Note：本程序提供excel文件转换为理正标准数据接口的功能")
    sleep(0.3)
    print("*************************************************************")
    sleep(1)

    filename, random_rqd = get_filename()
    print(filename)

    if random_rqd:
        print("进入生产随机RQD功能")
    else:
        output_file_name = result(filename)
        print("info:转换完成，转换后接口文件为：\n" + output_file_name.split("\\")[-1] + "\n")
        print('***info：导入到理正勘察前请务必备份理正数据库***\n')
        sleep(0.3)
        print("导入方法：①理正勘察8.5选择 接口→读入理正标准数据接口\n          ②理正勘察9.0选择 接口→读入旧版理正标准数据接口\n")
        sleep(0.3)

    input("info:按任意键退出...")


def testTimelimit():
    startTime, nowTime, endTime = get_time()

    if startTime < nowTime < endTime:
        return True
    else:
        print("\nerror:当前系统日期" + nowTime.strftime('%Y-%m-%d') + "已经超过本测试版使用期限，请到项目网站下载最新版或联系作者获取\n")
        return False


if __name__ == '__main__':
    #import traceback

    # 验证系统时间，测试版专用
    if testTimelimit():
        try:
            main()

        except Exception:
            print("\n*************************************************************")
            print("错误信息 debug：")
            #traceback.print_exc()
            print("*************************************************************")

            input("\nerror:程序运行异常...按下任意键退出")
    else:
        input("按任意键退出...")

