import datetime, csv

rows = []
title = ["CATEGORY", "PRODUCT", "COST", "DATE"]


def menu():
    menu_item = ["1. Add",
                 "2. Show all",
                 "3. Show for date",
                 "4. Show by category",
                 "5. Show by min->max",
                 "6. Delete",
                 "0. Exit"]

    def show_item():
        print()
        for item in menu_item:
            print(item)

    err_msg = "Введена недействительная команда. Необходимо ввести команду от 0 до 6"
    while True:
        show_item()
        try:
            choice = int(input("Введите команду: "))
        except ValueError:
            print(err_msg)
            continue

        if choice == 1:
            print("Add:")
            add_pur()
        elif choice == 2:
            print("Show all:")
            show_all()
        elif choice == 3:
            print("Show for date:")
            show_by(3)
        elif choice == 4:
            print("Show by category")
            show_by(0)
        elif choice == 5:
            print("Show by min->max COST:")
            sort_cost()
            show_all()
        elif choice == 6:
            print("Delete:")
            delete()
        elif choice == 0:
            print("Goodbye")
            break
        else:
            print(err_msg)


def input_date():
    """
    This function input and check date.
    :return: date
    """
    err_msg = "Введена недействительная дата. Необходимо дату в правильном формате"
    while True:
        try:
            year = int(input("Введите год: "))
            mon = int(input("Введите месяц: "))
            day = int(input("Введите день: "))
            dt = datetime.datetime(year, mon, day)
        except ValueError:
            print(err_msg)
            continue
        else:
            return dt


def add_pur():
    """
    This function input and adds in list new record
    :return:
    """
    row = []
    category = input("Введите категорию: ")
    prod = input("Введите продукт: ")
    while True:
        try:
            cost = int(input("Введите стоимость: "))
        except ValueError:
            print("Введите корректную стоимость.")
            continue
        else:
            break
    dt = input_date()
    row.append(category)
    row.append(prod)
    row.append(cost)
    row.append(str(dt.date()))
    rows.append(row)


def read_file():
    global rows
    try:
        with open('data.csv') as csvfile:
            inputcsv = csv.reader(csvfile, delimiter=',')
            rows = list(inputcsv)
    except IOError:
        print("Ошибка открытия файла базы данных.")
        exit(1)


def write_file():
    with open('data.csv', "w", newline="") as csvfile:
        output = csv.writer(csvfile)
        for row in rows:
            output.writerow(row)


def show_all():
    print("\n{: <20} {: <20} {: <20} {: <20}".format(*title))
    for row in rows:
        print("{: <20} {: <20} {: <20} {: <20}".format(*row))


def show_sel(column, choice):
    print("\n{: <20} {: <20} {: <20} {: <20}".format(*title))
    for row in rows:
        if row[column] == choice:
            print("{: <20} {: <20} {: <20} {: <20}".format(*row))


def sort_cost():
    """
    This function sorts list by cost increase.
    :return:
    """
    rows.sort(key=lambda row: int(row[2]))
    print("Sorted by COST")


def delete_record():
    global rows
    print("\n№   {: <20} {: <20} {: <20} {: <20}".format(*title))
    for id, row in enumerate(rows):
        print("{: <3} {: <20} {: <20} {: <20} {: <20}".format(id+1, *row))
    err_msg = "Введен неправильный номер записи. Необходимо ввести номер от 1 до " + str(len(rows))
    while True:
        try:
            choice = int(input("Для возврата в главное меню введите 0.\n"
                               "Введите номер записи, которую необходимо удалить: "))
        except ValueError:
            print(err_msg)
            continue
        if choice in range(1, len(rows)+1):
            print("Delete record № ", choice)
            answ = input("Подтвердите удаление записи Y/N: ")
            if answ == "Y":
                rows.pop(choice-1)
            print("Запись успешно удалена.")
            break
        elif choice == 0:
            print("Canceled")
            break
        else:
            print(err_msg)


def delete():
    global rows
    menu_item = ["1. Delete all list",
                 "2. Delete record",
                 "0. Cancel and return in main menu"]

    err_msg = "Введена недействительная команда. Необходимо ввести команду от 0 до 2"
    while True:
        print()
        for item in menu_item:
            print(item)
        try:
            choice = int(input("Введите команду: "))
        except ValueError:
            print(err_msg)
            continue

        if choice == 1:
            print("Delete all list:")
            answ = input("Подтвердите удаление всех записей: Y/N: ")
            if answ == "Y":
                rows.clear()
            break
        elif choice == 2:
            print("Delete record:")
            delete_record()
            break
        elif choice == 0:
            print("Canceled")
            break
        else:
            print(err_msg)


def show_by(column):
    category = set()
    for row in rows:
        category.add(row[column])
    tmp = list(category)
    for n, item in enumerate(tmp):
        print(n+1, item)

    err_msg = "Введен неправильный номер параметра. Необходимо ввести номер от 1 до " + str(len(category))
    while True:
        try:
            choice = int(
                input("Для возврата в главное меню введите 0.\nВведите номер параметра для выборки: "))
        except ValueError:
            print(err_msg)
            continue
        if choice in range(1, len(tmp) + 1):
            print(tmp[choice-1])
            show_sel(column, tmp[choice-1])

            break
        elif choice == 0:
            print("Canceled")
            break
        else:
            print(err_msg)


read_file()
menu()
write_file()

