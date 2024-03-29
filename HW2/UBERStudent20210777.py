#!/usr/bin/python3
import datetime
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

def getDay(month, date, year):
    d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return d[datetime.date(int(year), int(month), int(date)).weekday()]

dic = dict()
valDic = dict()
with open(inputfile, "rt") as f1:
    for line in f1:
        list = line.strip('\n').split(',')
        dayList = list[1].split('/')
        key = list[0] + "," + getDay(dayList[0], dayList[1], dayList[2])

        if key not in dic:
            dic[key] = list[2] + "," + list[3]
        else:
            tList = dic[key].split(',')
            temp1 = int(tList[0]) + int(list[2])
            temp2 = int(tList[1]) + int(list[3])
            dic[key] = str(temp1) + "," + str(temp2)
            
with open(outputfile, "wt") as f2:
    for k in dic.keys():
        f2.write(k + " " + dic[k] + "\n")

f1.close()
f2.close()
