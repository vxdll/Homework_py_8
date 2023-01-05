# Метод логирования

# Метод для записи результата в csv-формат
def ph_logger_csv(data):
    with open('ph_book.csv','a') as file:
        str_data = str.join(f'; ', data)
        file.write('{}\n'.format(str_data))

# Метод для записи результата в txt-формат
def ph_logger_txt(data):
    with open('ph_book.txt','a') as file:
        str = (f"Имя: {data[0]} \nФамилия: {data[1]} \nНомер телефона: {data[2]} \nОписание: {data[3]}\n\n")
        file.write(str)

