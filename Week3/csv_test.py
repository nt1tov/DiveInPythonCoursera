import csv

with open("cars.csv") as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    for row in reader:
        print(row)

xstr = '8x3x2.5'

x, y, z = xstr.split('x')
print(x, y, z)