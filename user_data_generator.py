import random
import os
from openpyxl import Workbook
from user_func import *


kol_vo = int(input("Введите кол-во строк:""\n"))
pol = int(input("Записи одного пола?""\n""1.да""\n""2.нет""\n"))
if pol == 1:
    opr_pol = int(input("Какой пол?""\n""1.мужской""\n""2.женский""\n"))
age = int(input("хотите выбрать определенный возраст?""\n""1.да""\n""2.нет""\n"))
opr_age = []
print(year)
if age == 1:
    while len(opr_age) != 2:
        opr_age.append(int(input("Введите сначала минимальный потом максимальный возраст""\n")))
town = []
s = int(input("хотите убрать определенные города""\n""1.да""\n""2.нет""\n"))
if s == 1:
    print(born_town)
    while "stop" not in town:
        town.append(input("Введите город из тех что видите выще чтобы не видеть его или не вводите ничего если подходят все города(stop чтобы закончить)""\n"))
    town_check = str()
data_base = {}
for i in range(kol_vo):
    if pol == 2:
        s = random.randint(a=1, b=2)
        if s == 1:
            data_base[i] = random.choice(names_m) + " "
            data_base[i] += random.choice(fam) + " "
            data_base[i] += "male" + " "
        elif s == 2:
            data_base[i] = random.choice(names_w) + " "
            data_base[i] += random.choice(fam) + " "
            data_base[i] += "female" + " "
    elif opr_pol == 1:
        data_base[i] = random.choice(names_m) + " "
        data_base[i] += random.choice(fam) + " "
        data_base[i] += "male" + " "
    elif opr_pol == 2:
        data_base[i] = random.choice(names_w) + " "
        data_base[i] += random.choice(fam) + " "
        data_base[i] += "female" + " "
    if len(opr_age) != 0:
        while age != "stop":
            age = random.choice(year)
            if int(age) >= int(min(opr_age)) and int(age) <= int(max(opr_age)):
                data_base[i] += str(age)
                data_base[i] += " "
                age = "stop"
    elif len(opr_age) == 0:
        data_base[i] += random.choice(year) + " "
    age = 0
    data_base[i] += random.choice(date) + " "
    if s == 1:
        town_check = random.choice(born_town)
        if town_check in town:
            data_base[i] += "0"
        elif town_check not in town:
            data_base[i] += town_check
    else:
        data_base[i] += random.choice(born_town)
# with open("data_base.xlsx", "w", encoding="UTF-8") as f:
#     for i in data_base.keys():
#         f.write(str(i))
#         f.write(" ")
#         f.write(data_base[i])
#         f.write("\n")
# workbook = Workbook()
# sheet = workbook.active
# header = ["id", "Имя", "Фамилия", "пол", "год рождения","день рождения","месяц рождения", "Город"]
# sheet.append(header)
# for i in data_base.keys():
#     j = data_base[i].split(maxsplit=6)
#     data = []
#     data.append(i)
#     data.extend(j)
#     print(data)
#     sheet.append(data)
# workbook.save("multiple_rows_example.xlsx")




















































