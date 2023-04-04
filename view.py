def First_screen():
    action = input(
        "Добро пожаловать в приложение Записки!\nВыберете действие:\n1 - Создать записку\n2 - Найти записку"
        "\n3 - Просмотреть все записки\n4 - Редактировать записку\n5 - Удалить записку\n6 - Выход\nВведите "
        "цифру действия --> ")
    while (int(action) < 1 or int(action) > 6):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    match action:
        case '1':
            print(1)
        case '2':
            print(2)
        case '3':
            print(3)
        case '4':
            print(4)
        case '5':
            print(5)
        case '6':
            print(6)