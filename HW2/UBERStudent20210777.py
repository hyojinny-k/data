#!/usr/bin/python3
from datetime import datetime, date
f1 = open("uber.dat", "rt")
#f1 = open("uber_exp.txt", "rt")
f2 = open("uberoutput.txt", "wt")
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
result = []
while True:
    row = f1.readline().replace("\n", "")
    if not row:
        break
    line = row.split(',')
    temp_date = line[1].split('/')
    m = int(temp_date[0])
    d = int(temp_date[1])
    y = int(temp_date[2])
    day = date(y, m, d).weekday()
    s = line[0] + ',' + days[day] + ' ' + line[2] + ',' + line[3] + '\n'
    result.append(s)

result.sort()
for r in result:
    f2.write(r)
f1.close()
f2.close()
