import os
import random
from card_generator import card
from choose_user import buyer,seller,admin
from data_base import nick_name


role = 1 #int(input("Выберете роль:\n1.покупатель\n2.продавец\n3.админ\n"))
if role == 1:
    with open("buyer_list.txt", "a+", encoding="utf-8") as f:
        f.write(random.choice(nick_name))
        f.write("\n")
    buyer()
elif role == 2:
    with open("seller_list.txt", "a+") as f:
        f.write(input("Введите имя пользователя\n" )+ "\n")
    seller()
elif role == 3:
    admin()

adress = input("Введите свой адресс""\n")

card(2)


































