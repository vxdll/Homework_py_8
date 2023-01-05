# Модуль поиска по базе данных

# Функция вывода для поиска
def show_data_srch(data):
    print(f"Найдено записей: {len(data)}\n")
    for i in data:
        str = (f"{i[0]} \n{i[1]} \n{i[2]} \n{i[3]}")
        print(str)

# Функции поиска контакта

# Функция для взаимодействия с пользователем
def search_data():
    type = int(input("1 - для поиска по имени или фамилии | 2 - для поиска по номеру: "))
    if type == 1:
        unknow = input("Введите имя или фамилию: ")
    elif type == 2:
        unknow = input("Введите номер телефона: ")
    else:
        print("Ошибка! Введите 1 или 2")
    return unknow

# Функция поиска контакта
def find_data(data):
    with open('ph_book.csv', 'r') as ph_bk:
        find_dt = []
        for i in ph_bk:
            for txt in i.split(";"):
                if data.lower() in txt.lower():
                    find = i.split(";")
                    find[0] = f"Имя: {find[0]}"
                    find[1] = f"Фамилия: {find[1]}"
                    find[2] = f"Номер телефона: {find[2]}"
                    find[3] = f"Описание: {find[3]}"
                    find_dt.append(find)
        show_data_srch(find_dt)