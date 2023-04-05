import json
from pathlib import Path
import view


def Create_note(name, text, create):
    db = Read_db()
    id = len(db)+1
    note = f"{id}; {name}; {text}; {create}"

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

def Find_numb(numb):
    db = Read_db()
    result = {}
    for item in db:
        for key, val in item.items():
            if numb == key:
                result = item
    return result

def Find_name(name):
    db = Read_db()
    result = {}
    for item in db:
        for key, val in item.items():
            if name in val[0]:
                result = item
    return result


def Find_text(text):
    db = Read_db()
    result = {}
    for item in db:
        for key, val in item.items():
            if text in val[1]:
                result = item
    return result

def Del_note(numb):
    db = Read_db()
    for i in range(len(db)-1):
        for key, val in db[i].items():
            if numb == key:
                db.remove(db[i])
    with open("notebooks.db", "w", encoding='utf-8') as file:
        for item in db:
            file.write(str(item))
        file.close()
    print("\n" * 100)
    print("Запись удалена")
    print("\n" * 3)
    view.Second_screen()



