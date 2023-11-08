#!/usr/bin/python3
from datetime import date
f1 = open("uber.dat", "rt")
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
    line[1] = days[day]
    result.append(line)

result.sort()
i = 1
while True:
    # f2.write(r)
    if result[i][0] == result[i - 1][0] and result[i][1] == result[i - 1][1]:
        result[i][2] = int(result[i][2]) + int(result[i-1][2])
        result[i][3] = int(result[i][3]) + int(result[i-1][3])
        del result[i-1]
    else:
        i += 1
    if i == len(result):
        break
for r in result:
    f2.write(r[0] + ',' + r[1] + ' ' + str(r[2]) + ',' + str(r[3]) + '\n')
f1.close()
f2.close()
