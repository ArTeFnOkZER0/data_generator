import random
from data_base import names_w,names_m,fam



def card(kol_vo):
    random_card = str()
    for i in range(kol_vo):
        bank = int(input("Введите какого банка нужна карта:""\n""1.мир""\n""2.VISA""\n""3.MasterCard""\n""4.American Express""\n"))
        if bank == 1:
            random_card += "2"
            for i in range(15):
                random_card += str(random.randint(a=0, b=9))
            random_card += "\n"
            random_card += str(random.randint(a=1, b=12))
            random_card += "/"
            random_card += str(random.randint(a=1, b=30))
            random_card += "/"
            random_card += str(random.randint(a=24, b=34))
            random_card += "\n"
            for i in range(3):
                random_card += str(random.randint(a=0, b=3))
            random_card += "\n"
            if random.randint(0,1):
                random_card += str(random.choice(names_m))
            else:
                random_card += str(random.choice(names_w))
            random_card += " "
            random_card += str(random.choice(fam))
        elif bank == 2:
            random_card += "4"
            for i in range(15):
                random_card += str(random.randint(a=0, b=9))
            random_card += "\n"
            random_card += str(random.randint(a=1, b=12))
            random_card += "/"
            random_card += str(random.randint(a=1, b=30))
            random_card += "/"
            random_card += str(random.randint(a=24, b=34))
            random_card += "\n"
            for i in range(3):
                random_card += str(random.randint(a=0, b=3))
            random_card += "\n"
            if random.randint(0, 1):
                random_card += str(random.choice(names_m))
            else:
                random_card += str(random.choice(names_w))
            random_card += " "
            random_card += str(random.choice(fam))
        elif bank == 3:
            random_card += "5"
            for i in range(15):
                random_card += str(random.randint(a=0, b=9))
            random_card += "\n"
            random_card += str(random.randint(a=1, b=12))
            random_card += "/"
            random_card += str(random.randint(a=1, b=30))
            random_card += "/"
            random_card += str(random.randint(a=24, b=34))
            random_card += "\n"
            for i in range(3):
                random_card += str(random.randint(a=0, b=3))
            random_card += "\n"
            if random.randint(0, 1):
                random_card += str(random.choice(names_m))
            else:
                random_card += str(random.choice(names_w))
            random_card += " "
            random_card += str(random.choice(fam))
        elif bank == 4:
            random_card += "34"
            for i in range(13):
                random_card += str(random.randint(a=0, b=9))
            random_card += "\n"
            random_card += str(random.randint(a=1, b=12))
            random_card += "/"
            random_card += str(random.randint(a=1, b=30))
            random_card += "/"
            random_card += str(random.randint(a=24, b=34))
            random_card += "\n"
            for i in range(3):
                random_card += str(random.randint(a=0, b=3))
            random_card += "\n"
            if random.randint(0, 1):
                random_card += str(random.choice(names_m))
            else:
                random_card += str(random.choice(names_w))
            random_card += " "
            random_card += str(random.choice(fam))



        random_card += "\n"
        random_card += "-" * 10
        random_card += "\n"
    print(random_card)