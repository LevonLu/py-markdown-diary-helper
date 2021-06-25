# -*- coding: UTF-8 -*-
from diaryhelper import *


class LawDairy:
    # 日记数量 总数 本年总数 本月总数
    diaryNumAll = 0
    diaryNumYear = 0
    diaryNumMonth = 0

    # 指令处理
    def function(self, strinput=""):
        strcommand = strinput.split(" ", 1)
        if strcommand[0] == "writenow" or strcommand[0] == "w":
            self.writenow()
        elif strcommand[0] == "create" or strcommand[0] == "c":
            if len(strcommand) == 1:
                self.create()
            else:
                self.create(strcommand[1])
        elif strcommand[0] == "merge" or strcommand[0] == "m":
            self.merge()
        elif strcommand[0] == "delete" or strcommand[0] == "d":
            if len(strcommand) == 1:
                self.delete()
            else:
                self.delete(strcommand[1])
        elif strcommand[0] == "show" or strcommand[0] == "s":
            if len(strcommand) == 1:
                self.show()
            else:
                self.show(strcommand[1])
        elif strcommand[0] == "open" or strcommand[0] == "o":
            if len(strcommand) == 1:
                self.open()
            else:
                self.open(strcommand[1])
        elif strcommand[0] == "help" or strcommand[0] == "h":
            self.help()
        elif strcommand[0] == "exit" or strcommand[0] == "e":
            exit(0)

    # 初始化 读取日记文件夹 统计数量
    def init(self):
        for tYear in range(2020, getYear() + 1):
            if os.path.exists(str(tYear)):
                for tMonth in range(1, 13, 1):
                    if os.path.exists(str(tYear) + "/" + str(tMonth)):
                        file_num = sum([os.path.isfile(listx) for listx in os.listdir("./")])
                        if file_num > 0:
                            this_month_diary = open(str(tYear) + "/" + str(tMonth).rjust(2, '0') + ".md", "w+")
                            this_month_diary.write(getmonthcover(tYear, tMonth))
                            for tDay in range(1, 31):
                                if os.path.isfile(getFileName(tYear, tMonth, tDay)):
                                    self.diaryNumAll += 1
                                    if getYear() == tYear:
                                        self.diaryNumYear += 1
                                    if getMonth() == tMonth:
                                        self.diaryNumMonth += 1

    # 展示日记本基本信息 篇数之类的
    def profile(self):
        strprofile = "日记总数:" + str(self.diaryNumAll) + "\n" + \
                     "本年度日记总数:" + str(self.diaryNumYear) + "\n" + \
                     "本月日记总数:" + str(self.diaryNumMonth)
        print(strprofile)

    # 立即写作(今天日记)
    def writenow(self):
        self.create()
        self.open()

    # 根据模板创建日记但不立即打开
    @staticmethod
    def create(date="today"):
        stryear, strmonth, strday = dateprocess(date)
        # 检查年份目录 若无则创建
        if not os.path.exists(stryear):
            os.mkdir(stryear)

        # 检查月份目录 若无则创建
        if not os.path.exists(stryear + "/" + strmonth):
            os.mkdir(stryear + "/" + strmonth)

        # 检查当天的日记文件是否创建 若无则创建 并写入基本信息
        strfilename = stryear + "/" + strmonth + "/" + strday + ".md"
        if not os.path.isfile(strfilename):
            TodayDiary = open(strfilename, 'w+')
            TodayDiary.write(getTimeTitle(date))
            TodayDiary.write(getDiaryHead())
            TodayDiary.close()
        print("Created:" + strfilename )

    # 合并日记
    @staticmethod
    def merge():
        for tYear in range(1998, getYear() + 1):
            if os.path.exists(str(tYear)):
                this_year_diary = open(str(tYear) + ".md", "w+")
                this_year_diary.write(getyearcover(tYear))
                for tMonth in range(1, 13, 1):
                    strmonth = str(tMonth).rjust(2, '0')
                    if os.path.exists(str(tYear) + "/" + strmonth):
                        file_num = sum([os.path.isfile(listx) for listx in os.listdir("./")])
                        if file_num > 0:
                            this_month_diary = open(str(tYear) + "/" + strmonth + ".md", "w+")
                            this_month_diary.write(getmonthcover(tYear, tMonth))
                            for tDay in range(1, 31):
                                if os.path.isfile(getFileName(tYear, tMonth, tDay)):
                                    file_day_diary = open(getFileName(tYear, tMonth, tDay), "r+", errors="ignore")
                                    str_day = file_day_diary.read()
                                    this_month_diary.write(str_day + "\n\n\n\n")
                                    file_day_diary.close()
                            this_month_diary.close()

                            file_month_diary = open(str(tYear) + "/" + strmonth + ".md", "r+", errors="ignore")
                            str_month = file_month_diary.read()
                            this_year_diary.write(str_month + "\n\n\n\n")
                            file_month_diary.close()
                this_year_diary.close()
        print("Merge finished")

    # 删除日记
    @staticmethod
    def delete(date="today"):
        stryear, strmonth, strday = dateprocess(date)
        strfilename = stryear + "/" + strmonth + "/" + strday + ".md"
        os.remove(strfilename)
        print("removed:" + strfilename)

    # 展示日历视图
    @staticmethod
    def show(viewmode="all"):
        # TODO 日历视图
        print(viewmode)

    # 打开某天日记
    @staticmethod
    def open(date="today"):
        stryear, strmonth, strday = dateprocess(date)
        strfilename = stryear + "/" + strmonth + "/" + strday + ".md"
        os.system("typora " + strfilename)

    # 帮助
    @staticmethod
    def help():
        strhelp = """
        指令可写全拼也可简写，指令与参数之间以空格隔开
        指令        简写  功能
        writenow    w   创建今天的日记文件并立即开始写作
        create      c   仅创建但不打开     create [date]
        merge       m   合并日记文件   
        delete      d   删除日记文件      delete [date]
        show        s   按日历视图显示     show [viewmode]
        open        o   打开日记文件      open [date]
        help        h   帮助
        exit        e   退出
        
        参数说明
        [date]  
            默认 表示今天
            yyyy.mm.dd : yyyy年mm月dd日
            mm.dd      : 今年mm月dd日
        [viewmode]  
            all 每个月
            month 本月
            year 本年按月显示
        """
        print(strhelp)
        return 1

    # 清屏
    @staticmethod
    def cls():
        os.system("cls")


if __name__ == '__main__':
    Mydiary = LawDairy()
    Mydiary.init()
    Mydiary.profile()

    while 1:
        strInput = input("->")
        Mydiary.function(strInput)
