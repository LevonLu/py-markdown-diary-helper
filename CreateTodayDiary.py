import os
import calendar
from MyTime import GetYear
from MyTime import GetMonth
from MyTime import GetDay
from MyTime import GetWeekdayStr
from MyTime import GetHour
from MyTime import GetMinute




def GetFileName():
    strFileName = str(GetYear()) + "/" + str(GetMonth()) + "/" +str(GetDay()) + ".md"
    return  strFileName

def GetTimeTitle():
    strTime = "## " + str(GetYear()) + "年" + str(GetMonth()) + "月" + str(GetDay()) + "日\t" + GetWeekdayStr() + "\n"
    return strTime

def GetDiaryHead():
    strHead = "> 天气\t:\t\n> 班休\t:\t\n> 时间\t:\t"+ str(GetHour()) + ":" + str(GetMinute()) + "\n\n\n\n***\n"
    return strHead

if __name__ == '__main__':
    # 检查年份目录 若无则创建
    if os.path.exists(str(GetYear())) == False:
        os.mkdir(str(GetYear()))

    # 检查月份目录 若无则创建
    if os.path.exists(str(GetYear()) + "/" + str(GetMonth())) == False:
        os.mkdir(str(GetYear()) + "/" + str(GetMonth()))

    # 检查当天的日记文件是否创建 若无则创建 并写入基本信息
    if os.path.isfile(GetFileName()) == False:
        TodayDiary = open(GetFileName(),'w+')
        TodayDiary.write(GetTimeTitle())
        TodayDiary.write(GetDiaryHead())
        TodayDiary.close()





