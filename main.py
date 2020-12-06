# -*- coding: UTF-8 -*-
#from MyTime import *
from diaryhelper import *

if __name__ == '__main__':
    # 检查年份目录 若无则创建
    if os.path.exists(str(getYear())) == False:
        os.mkdir(str(getYear()))

    # 检查月份目录 若无则创建
    if os.path.exists(str(getYear()) + "/" + str(getMonth())) == False:
        os.mkdir(str(getYear()) + "/" + str(getMonth()))

    # 检查当天的日记文件是否创建 若无则创建 并写入基本信息
    if os.path.isfile(getFileName()) == False:
        TodayDiary = open(getFileName(), 'w+')
        TodayDiary.write(getTimeTitle())
        TodayDiary.write(getDiaryHead())
        TodayDiary.close()

    mergeMonthDiary()