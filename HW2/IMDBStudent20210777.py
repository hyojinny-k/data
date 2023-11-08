#!/usr/bin/python3
f1 = open("movie.dat", "rt")
f2 = open("movieoutput.txt", "wt")
genre = []
while True:
    row = f1.readline().replace("\n", "")
    if not row:
        break
    line = row.split('::')
    if line[-1].find('|') > -1:
        temp_genre = line[-1].split('|')
        for g in temp_genre:
            genre.append(g)
    else:
        genre.append(line[-1])

list_genre = list(set(genre))
for g in list_genre:
    s = g + ' ' + str(genre.count(g)) + '\n'
    f2.write(s)
f1.close()
f2.close()
