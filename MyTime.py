import time

def GetYear():
    localtime = time.localtime(time.time())
    return localtime[0]

def GetMonth():
    localtime = time.localtime(time.time())
    return localtime[1]

def GetDay():
    localtime = time.localtime(time.time())
    return localtime[2]

def GetHour():
    localtime = time.localtime(time.time())
    return localtime[3]

def GetMinute():
    localtime = time.localtime(time.time())
    return localtime[4]

def GetSecond():
    localtime = time.localtime(time.time())
    return localtime[5]

def GetWeekday():
    localtime = time.localtime(time.time())
    return localtime[6]

def GetWeekdayStr():
    strWeek = "星期日","星期一","星期二","星期三","星期四","星期五","星期六"
    return strWeek[GetWeekday()]