# -*- coding: UTF-8 -*-
import time
import calendar

# 今儿几几年
def getYear():
    localtime = time.localtime(time.time())
    return localtime[0]

# 今儿哪月
def getMonth():
    localtime = time.localtime(time.time())
    return localtime[1]

# 今儿哪天
def getDay():
    localtime = time.localtime(time.time())
    return localtime[2]

# 现在几点
def getHour():
    localtime = time.localtime(time.time())
    return localtime[3]

# 现在几分
def getMinute():
    localtime = time.localtime(time.time())
    return localtime[4]

# 现在几秒。。过分了
def getSecond():
    localtime = time.localtime(time.time())
    return localtime[5]

# 今儿周几 返回一个星期编码
def getWeekday():
    localtime = time.localtime(time.time())
    return localtime[6]

# 今儿周几，说人话 返回星期几的汉语字符串
def getWeekdayStr():
    strWeek = "星期一","星期二","星期三","星期四","星期五","星期六","星期日"
    return strWeek[getWeekday()]

# 这个月有几天 无参时表示获取当前月的天数，也可指定参数
def getMonthDays(year = 0,month = 0):
    if year == 0 or month == 0:
        return calendar.monthrange(getYear(), getMonth())
    else:
        return calendar.monthrange(year,month)
