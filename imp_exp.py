# Модуль импорта и экспорта данных

# Функция импорта данных
def write_data():
    data = [input("Введите имя: ").title(), input("Введите Фамилию: ").title()]
    tel_number = input("Введите номер телефона: ")
    data.append(tel_number)
    another = input("Введите описание: ")
    data.append(another)
    return data

# Функция экспорта данных
def ext_data():
    with open('ph_book.csv', 'r') as ph_bk:
        data = []
        for i in ph_bk:
            data.append(i.replace(';', ', ').replace('\n', ''))
        show_data(data)

# Функция вывода
def show_data(data):
    print(f"Найдено записей: {len(data)}")
    for i in data:
        print(i)