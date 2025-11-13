import requests

c = {}

file = requests.get("http://dfedorov.spb.ru/python3/sport.txt")
file.encoding = "cp1251"
data = file.text.strip().split("\n")

for line in data[1:]:
    iou = line.split('\t')
    if len(iou) > 5:
        sport = iou[3]
        sport = sport.replace(';', ',')
        sports = sport.split(',')
        for line2 in sports:
            line2 = line2.strip().lower()
            if line2 != '':
                if line2 in c:
                    c[line2] = c[line2] + 1
                else:
                    c[line2] = 1
sort = sorted(c, key=c.get, reverse=True)

print('Самые популярные виды спорта:\n '
      'Место     Спорт    Кол-во')

print(f'1 место - {sort[0]} - {c[sort[0]]}\n'
      f'2 место - {sort[1]} - {c[sort[1]]}\n'
      f'3 место - {sort[2]} - {c[sort[2]]}\n')
