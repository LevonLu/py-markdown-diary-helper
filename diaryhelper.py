# -*- coding: UTF-8 -*-
import os
from MyTime import *


# 获取文件路径，有参数时按照参数的日期获取文件路径，无参数时返回今日文件路径
def getFileName(year = 0, month = 0, day = 0):
    strFileName = ""
    if year == 0:
        strFileName = str(getYear()) + "/" + str(getMonth()).rjust(2, '0') + "/" +str(getDay()).rjust(2, '0') + ".md"
    else:
        strFileName = str(year) + "/" + str(month).rjust(2, '0') + "/" + str(day).rjust(2, '0') + ".md"
    return  strFileName

# 返回当日日记标题
def getTimeTitle(date="today"):
    stryear, strmonth, strday = dateprocess(date)
    strTime = "## " + stryear + "年" + strmonth + "月" + strday + "日\t" + getWeekdayStr(date) + "\n\n"
    return strTime

# 返回当日日记开头
def getDiaryHead():
    strHour = str(getHour()).rjust(2, '0')
    strMinute = str(getMinute()).rjust(2, '0')
    strHead = "> 天气\t:\t\n> 班休\t:\t\n> 时间\t:\t"+ strHour + ":" + strMinute + "\n\n\n\n***\n\n"
    return strHead

# 返回月汇总日记的封面
def getmonthcover(year = 0,month = 0):
    strCover = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<center><font size=30> " + str(year) + "." + str(month).rjust(2, '0') + "</font></center>" + "\n<div STYLE=\"page-break-after: always;\"></div>\n"
    return strCover

# 返回年汇总日记的封面
def getyearcover(year = 0):
    strCover = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<center><font size=60> " + str(year) + "</font></center>" + "\n<div STYLE=\"page-break-after: always;\"></div>\n"
    return strCover

# 合并文件夹 从2020年开始 遍历每一个文件夹
def MergeDiary():
    for tYear in range(2020, getYear() + 1):
        if (os.path.exists(str(tYear))):
            this_year_diary = open(str(tYear) + ".md", "w+")
            this_year_diary.write(getyearcover(tYear))
            for tMonth in range(1,13,1):
                if(os.path.exists(str(tYear) + "/" + str(tMonth).rjust(2, '0'))):
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

                        file_month_diary = open(str(tYear) + "/" + str(tMonth).rjust(2, '0') + ".md", "r+", errors="ignore")
                        str_month = file_month_diary.read()
                        this_year_diary.write(str_month + "\n\n\n\n")
                        file_month_diary.close()
            this_year_diary.close()








