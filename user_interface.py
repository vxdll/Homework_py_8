# Функкиця интерфейса
def menu():
    print("*"*10, "Добро пожаловать в телефонный справочник!", "*"*10)
    mode = input("1 - Для импорта данных \n2 - Для экспорта данных \n3 - Для поиска контакта \n4 - Выход \nВвод: ")
    if mode in "1234":
        return int(mode)
    else:
        print("Ошибка ввода!!! Попробуйте ещё раз!")


