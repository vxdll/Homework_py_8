# Функция для работы со справочником
import user_interface as ui
import logger as log
import search as s
import imp_exp as ie

def ph_book():
    while True:
        sel = ui.menu()
        if sel == 1:
            user = ie.write_data()
            log.ph_logger_csv(user)
            log.ph_logger_txt(user)
        elif sel == 2:
            ie.ext_data()
        elif sel == 3:
            found = s.search_data()
            s.find_data(found)
        elif sel == 4:
            print("Выход")
            exit()