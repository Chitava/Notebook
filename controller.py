import json
from pathlib import Path
import view
import datetime


def Create_note():
    print("\n" * 100)
    today = datetime.datetime.today()
    today = today.strftime("%m/%d/%Y")
    name = input('Введите название записи и нажмите "Enter"\n')
    text = input('Напишите техт заметки и нажмите "Enter"\n')
    db = Read_db()
    id = len(db)+1
    note = f"{id}; {name}; {text}; {today}"
    with open("notebooks.cvs", "a", encoding='utf-8') as file:
        file.write(f'\n{note}')
        file.close()
    print("\n"*100)
    print("Запись сохранена\n")
    view.Second_screen()

def Read_db():
    notes = []
    with open("notebooks.cvs", "r", encoding='utf-8') as file:
        temp = []
        while True:
            temp_note = {}
            val = []
            line = file.readline().replace("\n", "")
            if line != "":
                temp= line.split(";")
            else:
                break
            val.append(temp[1])
            val.append(temp[2])
            val.append(temp[3])
            temp_note[temp[0]] = val
            notes.append(temp_note)
        file.close()
    return notes


def Find():
    print("\n" * 100)
    action = input(
        "Выберете метод поиска:\n1 - по номеру:\n2 - по названию:\n3 - по содержимому:"
        "\n4 - по дате:\n5 - выход в главное меню:\n6 - Выход из программы\nВведите цифру действия --> ")
    while (int(action) < 1 or int(action) > 6):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    match action:
        case '1':
            print("\n" * 100)
            action = input("Введите номер записи -->")
            db = Read_db()
            for item in db:
                for key, val in item.items():
                    if action == key:
                        Print_note(item)
            view.Second_screen()
        case '2':
            print("\n" * 100)
            action = input("Введите название записи -->")
            db = Read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[0]:
                        Print_note(item)
            view.Second_screen()
        case '3':
            print("\n" * 100)
            action = input("Введите строку поиска -->")
            db = Read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[1]:
                        Print_note(action)
            view.Second_screen()
        case '4':
            print("\n" * 100)
            action = input("Введите число, либо месяц, либо год создания -->")
            db = Read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[2]:
                        Print_note(action)
            view.Second_screen()
        case '5':
            print("\n" * 100)
            view.Second_screen()
        case '6':
            exit()

def Del_note(numb):
    db = Read_db()
    for i in range(len(db)-1):
        for key, val in db[i].items():
            if numb == key:
                db.remove(db[i])
    with open("notebooks.cvs", "w", encoding='utf-8') as file:
        for item in db:
            file.write(str(item))
        file.close()
    print("\n" * 100)
    print("Запись удалена")
    print("\n" * 3)
    view.Second_screen()


def Print_note(note):
    result = []
    for keys, val in note.items():
        result.append(val[0])
        result.append(val[1])
        result.append(val[2])
        if len(val) > 3:
            result.append(val[3])
    if len(result) == 0:

        print("\nЗаписи с таким номер не существует")
    else:
        print(f"\nЗапись № {keys}\nНазвание{result[0]}\n{result[1]}\nДата создания{result[2]}")
    if len(note.values()) == 4:
        print(f"Дата последнего изменения {result[3]}")


def Show_all():
    db = Read_db()
    for item in db:
        result = []
        for keys, val in item.items():
            result.append(val[0])
            result.append(val[1])
            result.append(val[2])
            if len(val) > 3:
                result.append(val[3])
            if len(result) == 0:
                print("Записей нет")
            else:
                print(f"\nЗапись № {keys}\nНазвание{result[0]}\n{result[1]}\nДата создания{result[2]}")
            if len(item.values()) == 4:
                print(f"Дата последнего изменения {result[3]}")

    view.Second_screen()


def Edit_note():
    numb = input("\nВведите номер редактируемой записи:\n--> ")
    db = Read_db()
    edit = {}
    for item in db:
        for key, val in item.items():
            if numb == key:
                edit = item
    for i in range(len(db)-1):
        for key, val in db[i].items():
            if numb == key:
                db.remove(db[i])
    action = input(
        "Выберете пункт редактирования:\n1 - название:\n2 - содержимое:\nВведите пункт --> ")
    while (int(action) < 1 or int(action) > 2):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    today = datetime.datetime.today()
    today = today.strftime("%m/%d/%Y")
    Print_note(edit)
    match action:
        case '1':
            print("\n")
            result = []
            for keys, val in edit.items():
                result.append(val[1])
                result.append(val[2])
            action = input("Введите новое название --> ")
            new_note = {}
            new_note[numb] = [action, result[0], result[1], today]
            db.append(new_note)
            with open("notebooks.cvs", "w", encoding='utf-8') as file:
                for i in range(len(db)):
                    item = str(db[i]).replace("{", "").replace("}", "").replace("'", "").replace(":", ",")\
                        .replace("[", "").replace("]", "").replace(",", ";")
                    if i == (len(db) - 1):
                        file.write(f'{item}')
                    else:
                        file.write(f'{item}\n')
                file.close()

            # print("\n" * 100)
            print("Запись сохранена\n")
            view.Second_screen()
        case '2':
            print("\n")
            result = []
            for keys, val in edit.items():
                result.append(val[0])
                result.append(val[2])
            action = input("Введите новое название --> ")
            new_note = {}
            new_note[numb] = [result[0], action, result[1], today]
            db.append(new_note)
            with open("notebooks.cvs", "w", encoding='utf-8') as file:
                for i in range(len(db)):
                    item = str(db[i]).replace("{", "").replace("}", "").replace("'", "").replace(":", ",") \
                        .replace("[", "").replace("]", "").replace(",", ";")
                    if i == (len(db) - 1):
                        file.write(f'{item}')
                    else:
                        file.write(f'{item}\n')
                file.close()
            print("Запись сохранена\n")
            view.Second_screen()
            print("\n")
            action = input("Введите новый текст -->")
            db = Read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[0]:
                        Print_note(item)
            view.Second_screen()