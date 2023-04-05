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
            controller.Create_note()
        case '2':
            controller.Find()
        case '3':
            controller.Show_all()
        case '4':
            print(4)
        case '5':
            controller.Del_note()
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
            controller.Create_note()
        case '2':
            controller.Find()
        case '3':
            controller.Show_all()
        case '4':
            print(4)
        case '5':
            controller.Del_note()
        case '6':
            exit()


