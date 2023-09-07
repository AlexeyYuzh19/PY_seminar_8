'''
8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
Информация о человеке: Фамилия, Имя, Телефон, Описание
Корректность и уникальность данных не обязательны.
Функционал программы
1) телефонный справочник хранится в памяти в процессе выполнения кода.
Выберите наиболее удобную структуру данных для хранения справочника.
2) CRUD: Create, Read, Update, Delete
Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
(*) Усложнение. Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
Delete: Удаление записи из справочника. Выбор - как в Read.
3) экспорт данных в текстовый файл формата csv
4) импорт данных из текстового файла формата csv
Используйте функции для реализации значимых действий в программе
'''

# импорт модулей
import csv
import time

phonebook = []

# функция для добавления новой записи в справочник
def create_record():
    last_name = input("Введите Фамилию : ")
    while not last_name.isalpha():
        print("\033[31mОшибка!\033[0m Введите только текст.")
        last_name = input("Введите Фамилию : ")
    first_name = input("Введите Имя : ")
    while not first_name.isalpha():
        print("\033[31mОшибка!\033[0m Введите только текст.")
        first_name = input("Введите Имя : ")
    phone_number = input("Введите номер телефона : ")
    while not (phone_number.startswith("+7") and phone_number[1:].isdigit() and len(phone_number[1:])== 11):
        print("\033[31mОшибка!\033[0m Номер телефона должен начинаться с +7 и состоять из 11 цифр.")
        phone_number = input("Введите номер телефона : ")
    email = input("Введите адрес электронной почты : ")
    while not (email.count("@") == 1 and email.count(".") >= 1):
        print("\033[31mОшибка!\033[0m Введите корректный адрес электронной почты.")
        email = input("Введите адрес электронной почты : ")    
    description = input("Введите комментарий : ")
    record = {"last_name": last_name, "first_name": first_name, "phone_number": phone_number, "email": email, "description": description}    
    phonebook.append(record)
    print("Запись добавлена.")

# функция для выбора записей из справочника по фамилии
def search_records():  
    search_param = input("Введите параметр поиска - Имя, Фамилия, телефон : ")  
    for record in phonebook:  
        if (record["last_name"].startswith(search_param) or   
            record["first_name"].startswith(search_param) or   
            record["phone_number"].startswith(search_param)):  
            print("Имя : ", record["first_name"])  
            print("Фамилия : ", record["last_name"])  
            print("Номер телефона : ", record["phone_number"])  
            print("Электронная почта : ", record["email"])  
            print("Комментарий : ", record["description"])  
            confirm = input("Перейти к следующему действию - ( да ) : ")  
            if confirm.lower() == "да":  
                return  
            else: 
                continue 
    print("Запись не найдена.")
    
# функция для изменения данных выбранной записи в справочнике
def update_record():
    last_name = input("Введите Имя или Фамилию для поиска : ")
    for record in phonebook:
        if record["last_name"].startswith(last_name) or record["first_name"].startswith(last_name):
            print("Имя : ", record["first_name"])
            print("Фамилия : ", record["last_name"])
            print("Номер телефона : ", record["phone_number"])
            print("Адрес электронной почты : ", record["email"])
            print("Комментарий : ", record["description"])
            choice = input("Хотите изменить данные? ( да/нет ) : ")
            if choice.lower() == "да":
                new_last_name = input("Введите Фамилию : ")
                while not new_last_name.isalpha():
                    print("\033[31mОшибка!\033[0m Введите только текст.")
                    new_last_name = input("Введите Фамилию : ")
                new_first_name = input("Введите Имя : ")
                while not new_first_name.isalpha():
                    print("\033[31mОшибка!\033[0m Введите только текст.")
                    new_first_name = input("Введите Имя : ")
                new_phone_number = input("Введите номер телефона : ")
                while not (new_phone_number.startswith("+7") and new_phone_number[1:].isdigit() and len(new_phone_number[1:])== 11):
                    print("\033[31mОшибка!\033[0m Номер телефона должен начинаться с +7 и состоять из 11 цифр.")
                    new_phone_number = input("Введите номер телефона : ")
                new_email = input("Введите адрес электронной почты : ")
                while not (new_email.count("@") == 1 and new_email.count(".") >= 1):
                    print("\033[31mОшибка!\033[0m Введите корректный адрес электронной почты.")
                    new_email = input("Введите адрес электронной почты : ")
                record["first_name"] = new_first_name
                record["last_name"] = new_last_name
                record["phone_number"] = new_phone_number
                record["email"] = new_email
                record["description"] = input("Введите комментарий : ")
                print("Запись изменена.")
            return
    print("Запись не найдена.")

# функция для удаления выбранной записи из справочника
def delete_record():
    last_name = input("Введите Имя или Фамилию : ")
    for record in phonebook:
        if record["last_name"].startswith(last_name) or record["first_name"].startswith(last_name):
            print("Запись найдена : ")
            print(record)
            confirm = input("Вы уверены, что хотите удалить запись? (да / нет) : ")
            if confirm.lower() == "да":
                phonebook.remove(record)
                print("Запись удалена.")
            else:
                print("Удаление отменено.")
            return
    print("Запись не найдена.")
    
# функция для экспорта данных справочника в файл csv
def export_data():    
    filename = input("Введите имя файла для экспорта записей : ")    
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:        
        writer = csv.DictWriter(csvfile, fieldnames=["last_name", "first_name", "phone_number", "email", "description"])        
        writer.writeheader()        
        for record in phonebook:
            writer.writerow(record)
    print("Данные экспортированы.")
    
# функция для импорта данных справочника из файла csv
def import_data():
    filename = input("Введите имя файла для импорта : ")    
    with open(filename, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phonebook.append(row)
    print("Данные импортированы.")
    print(phonebook)

# функция для печати содержимого справочника
def print_records():       
    if len(phonebook) == 0:
        print("\033[33mСправочник не заполнен.\033[0m\n")
    else:
        for record in phonebook:   
            print("Имя : ", record["first_name"])   
            print("Фамилия : ", record["last_name"])   
            print("Номер телефона : ", record["phone_number"])   
            print("Электронная почта : ", record["email"])   
            print("Комментарий : ", record["description"]) 
            print()
    
# код программы
while True:    
    time.sleep(2)   
    print(" ' 1 ' -  Создать запись.")
    print(" ' 2 ' -  Найти запись.")
    print(" ' 3 ' -  Изменить запись.")
    print(" ' 4 ' -  Удалить запись.")
    print(" ' 5 ' -  Экспорт данных.")
    print(" ' 6 ' -  Импорт данных.")
    print(" ' 7 ' -  Печать справочника.")
    print(" ' 0 ' -  Выйти из справочника.")    
    choice = input("\033[32mВведите номер действия \033[0m: ")    
    if choice == "1":
        create_record()
        time.sleep(2)
    elif choice == "2":
        search_records()
    elif choice == "3":
        update_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        export_data()
    elif choice == "6":
        import_data()
    elif choice == "7":
        print("\033[36m\nСодержание записей справочника.\033[0m\n")
        print_records()
    elif choice == "0":
        break
    else:        
        print("\033[31mОшибка!\033[0m Неверный выбор.")