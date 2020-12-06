import csv
import math
file = open('latandlon.csv', 'w', encoding = 'utf-8', newline='')
f = csv.writer(file)
csv_file=csv.reader(open('latlon.csv','r'))
for line in csv_file:
    row = (int(line[0]) - 171) / 854 * 600
    col = (int(line[1]) - 445) / 1280 * 1200
    f.writerow([round(row), round(col), line[2], line[3]])

file.close()