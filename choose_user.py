

def buyer():
    action = 0
    member = str()
    while action != 3:
        action = int(input("Выберите действие:\n1.Просмотр товаров.\n2.Добавить товар в корзину.\n3.остановить работу.\n"))
        if action == 1:
            with open("buy_list.txt", "r", encoding="UTF-8") as f:
                s = f.read()
                print(s)
                member += "Просмотр товаров." + "\n"

        if action == 2:
                with open("grocery_basket.txt", "a+", encoding="utf-8") as f:
                    f.write(input("Введите что хотите добавить из списка" + "\n") + "\n")
                    member += "Добавить товар в корзину." + "\n"
    print(member)

def seller():
    member = str()
    action = 0
    while action != 3:
        action = int(input("Выберите действие:\n1.Удаление товара.\n2.Добавить товар в корзину.\n3.остановить работу.\n"))
        if action == 1:
            with open("grocery_basket.txt", "r") as f:
                lines = f.readlines()
                indexes = int(input('Введите товар который нужно удалить: '))
                del lines[indexes]
            with open("grocery_basket.txt", "w") as f:
                f.writelines(lines)
                member += "удаление товара"
        if action == 2:
            with open("grocery_basket.txt", "a+") as f:
                f.write(input("Введите что хотите добавить из списка" + "\n") + "\n")
                member += "Добавить товар в корзину." + "\n"

def admin():
    member = str()
    action = 0
    while action != 3:
        action = int(input("Выберите действие:\n1.Удаление товара.\n2.Редактировать пользователей.\n3.остановить работу.\n"))
        if action == 1:
            with open("grocery_basket.txt", "r") as f:
                lines = f.readlines()
                indexes = int(input('Введите товар который нужно удалить: '))
                del lines[indexes]
            with open("grocery_basket.txt", "w") as f:
                f.writelines(lines)
            member += "удаление товара"
        if action == 2:
            user_tipe = int(input("Выберите тип пользователей который хотите редактировать:\n1.покупатель.\n2.продавец\n"))
            if user_tipe == 1:
                with open("buyer_list.txt", "r") as f:
                    lines = f.readlines()
                    indexes = int(input('Введите номер пользователя который нужно удалить: '))
                    del lines[indexes]
                with open("buyer_list.txt", "w") as f:
                    f.writelines(lines)
                member += "Редактировать пользователей" + "/" + "покупатель"
            if user_tipe == 2:
                with open("seller_list.txt", "r") as f:
                    lines = f.readlines()
                    indexes = int(input('Введите номер пользователя который нужно удалить: '))
                    del lines[indexes]
                with open("seller_list.txt", "w") as f:
                    f.writelines(lines)
                member += "Редактировать пользователей" + "/" + "продавец"
    print(member)

