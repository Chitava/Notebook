import datetime
import controller



def First_screen():
    action = ''
    action = input(
        "Добро пожаловать в приложение Записки!\nВыберете действие:\n1 - Создать записку\n2 - Найти записку"
        "\n3 - Просмотреть все записки\n4 - Редактировать записку\n5 - Удалить записку\n6 - Выход из программы\nВведите "
        "цифру действия --> ")
    while (int(action) < 1 or int(action) > 6):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    match action:
        case '1':
            Create()
        case '2':
            Find()
        case '3':
            Show_all()
        case '4':
            print(4)
        case '5':
            Del_note()
        case '6':
            exit()


def Second_screen():
    action = input(
        "\nПродолжаем работать в приложении!\nВыберете действие:\n1 - Создать записку\n2 - Найти записку"
        "\n3 - Просмотреть все записки\n4 - Редактировать записку\n5 - Удалить записку\n6 - Выход из программы\nВведите "
        "цифру действия --> ")
    while (int(action) < 1 or int(action) > 6):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    match action:
        case '1':
            Create()
        case '2':
            Find()
        case '3':
            Show_all()
        case '4':
            print(4)
        case '5':
            Del_note()
        case '6':
            exit()

def Create():
    print("\n" * 100)
    today = datetime.datetime.today()
    today = today.strftime("%m/%d/%Y")
    name = input('Введите название записи и нажмите "Enter"\n')
    text = input('Напишите техт заметки и нажмите "Enter"\n')
    controller.Create_note(name, text, today)
    Second_screen()


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
            note = controller.Find_numb(action)
            key = list(note.keys())
            result = []
            for keys, val in note.items():
                result.append(val[0])
                result.append(val[1])
                result.append(val[2])
                if len(val) > 3:
                    result.append(val[3])
            if len(result) == 0:
                print("Записи с таким номер не существует")
            else:
                print(f"Запись № {key[0]}\nНазвание{result[0]}\n{result[1]}\nДата создания{result[2]}")
            if len(note.values()) == 4:
                print(f"Дата последнего изменения {result[3]}")
            Second_screen()
        case '2':
            print("\n" * 100)
            action = input("Введите название записи -->")
            note = controller.Find_name(action)
            key = list(note.keys())
            result = []
            for keys, val in note.items():
                result.append(val[0])
                result.append(val[1])
                result.append(val[2])
                if len(val) > 3:
                    result.append(val[3])
            if len(result) == 0:
                print("Записи с таким номер не существует")
            else:
                print(f"Запись № {key[0]}\nНазвание{result[0]}\n{result[1]}\nДата создания{result[2]}")
            if len(note.values()) == 4:
                print(f"Дата последнего изменения {result[3]}")
            Second_screen()
        case '3':
            print("\n" * 100)
            action = input("Введите название записи -->")
            note = controller.Find_text(action)
            key = list(note.keys())
            result = []
            for keys, val in note.items():
                result.append(val[0])
                result.append(val[1])
                result.append(val[2])
                if len(val) > 3:
                    result.append(val[3])
            if len(result) == 0:
                print("Записи с таким номер не существует")
            else:
                print(f"Запись № {key[0]}\nНазвание{result[0]}\n{result[1]}\nДата создания{result[2]}")
            if len(note.values()) == 4:
                print(f"Дата последнего изменения {result[3]}")
            Second_screen()
        case '4':
            print("\n" * 100)
            Second_screen()
        case '5':
            print("\n" * 100)
            Second_screen()
        case '6':
            exit()


def Del_note():
    # print("\n" * 100)
    action = input("Введите номер записи которую нужно удалить -->")
    controller.Del_note(action)
    Second_screen()


def Show_all():
    db = controller.Read_db()
    result = []
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

    Second_screen()