# -*- coding: UTF-8 -*-
import os
from MyTime import *

# 获取文件路径，有参数时按照参数的日期获取文件路径，无参数时返回今日文件路径
def getFileName(year = 0, month = 0, day = 0):
    strFileName = ""
    if year == 0:
        strFileName = str(getYear()) + "/" + str(getMonth()) + "/" +str(getDay()) + ".md"
    else:
        strFileName = str(year) + "/" + str(month) + "/" + str(day) + ".md"
    return  strFileName

# 返回当日日记标题
def getTimeTitle():
    strTime = "## " + str(getYear()) + "年" + str(getMonth()) + "月" + str(getDay()) + "日\t" + getWeekdayStr() + "\n\n"
    return strTime

# 返回当日日记开头
def getDiaryHead():
    strHead = "> 天气\t:\t\n> 班休\t:\t\n> 时间\t:\t"+ str(getHour()) + ":" + str(getMinute()) + "\n\n\n\n***\n\n"
    return strHead

# 返回月汇总日记的封面
def getmonthcover(year = 0,month = 0):
    strCover = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<center><font size=30> " + str(year) + "." + str(month) + "</font></center>" + "\n<div STYLE=\"page-break-after: always;\"></div>\n"
    return strCover

# 合并文件夹 从2020年开始 遍历每一个文件夹
def mergeMonthDiary():
    for tYear in range(2020, getYear() + 1):
        if (os.path.exists(str(tYear))):
            for tMonth in range(1,13,1):
                if(os.path.exists(str(tYear) + "/" + str(tMonth))):
                    file_num = sum([os.path.isfile(listx) for listx in os.listdir("./")])
                    if file_num > 0:
                        this_month_diary = open(str(tYear) + "/" + str(tMonth) + ".md","w+")
                        this_month_diary.write(getmonthcover(tYear,tMonth))
                        for tDay in range(1,31):
                            if os.path.isfile(getFileName(tYear,tMonth,tDay)):
                                file_day_diary = open(getFileName(tYear,tMonth,tDay),"r+", errors = "ignore")
                                str_day = file_day_diary.read()
                                this_month_diary.write(str_day + "\n\n\n\n")
                                file_day_diary.close()
                        this_month_diary.close()







