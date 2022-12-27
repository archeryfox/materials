import csv
import sys
from tabulate import tabulate
isnext = False
def main():
    """
    Данная функция выполняет функции консольного меню, предоставляя возможность авторизации, регистрации, и выхода пользователя.
    :return: Данная функция ничего не возвращает.
    """
    while True:
        key = ""
        try:
            key = int(input("Добро пожаловать!\n1. Зарегистрироваться\n2. Войти\n3. Закрыть программу\n"))
        except:
            print("Вы ввели данные в неверном формате. Нужен тип integer.")
            main()
        if key == 1:
            reg()
        elif key == 2:
            autorize()
        elif key == 3:
            sys.exit()
        else:
            print("Такой операции не найдено. Выберите или 1 или 2 или 3.")
            main()
def reg():
    """
    Данная функция проводит регистрацию пользователя, прося его логин и повторение пароля. В случае занятого логина,
    пользователя переводит в поле авторизации, в случае неверного повторения пароля - в регистрацию. После,
    функция вызывает доп.функцию regcontinue, которая записывает логин и пароль в базу данных пользователей.
    :return: Данная функция ничего не возвращает.
    """
    reglogin = ""
    try:
        reglogin = input("Введите желаемый логин - ")
    except:
        print("Ошибка. Попробуйте еще раз. Тип данных - string.")
        reg()
    logfile = logfiles()
    logins = logfile[0]
    loginexist = reglogin in logins
    if loginexist:
        print("Логин уже занят. Переводим вас в поле авторизации.")
        autorize()
    try:
        regpassword = input("Введите желаемый пароль - ")
        if regpassword != input("Повторите пароль - "):
            print("Неверно повторен пароль.")
            reg()
        else:
            regcontinue(reglogin, regpassword)
    except:
        print("Ошибка. Попробуйте еще раз. Тип данных - string.")
        reg()
def regcontinue(reglogin : str, regpassword : str):
    """
    Данная функция записывает данные пользователя в файл.
    :param reglogin: Логин, введенный пользователем
    :param regpassword: Пароль, введенный пользователем
    :return: Данная функция ничего не возвращает
    """
    with open("user.csv", "a") as file:
        file.write(f"\n{reglogin},{regpassword},user")
    file.close()
    print("Регистрация завершена.")
    main()
def logfiles():
    """
    Данная функция считывает логины, пароли и роли пользователей и возвращает их.
    :return: Список логинов, паролей и ролей пользователей.
    """
    logins = []
    passwords = []
    roles = []
    with open("user.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for read in reader:
            logins.append(read[0])
            passwords.append(read[1])
            roles.append(read[2])
    file.close()
    return [logins, passwords, roles]
def autorize():
    """
    Данная функция служит входом в систему для уже зарегистрированных пользователей. В случае удачной регистрации
    входящего переносит в функцию user или administrator, в зависимости от его роли. В случае неудачной - переносит
    его в консольное меню.
    :return: Данная функция ничего не возвращает
    """
    login = ""
    password = ""
    role = ""
    try:
        login = input("Авторизация. Введите ваш логин - ")
    except:
        print("Неверно введены данные. Тип данных - string.")
        autorize()
    try:
        password = input("Введите ваш пароль - ")
    except:
        print("Неверно введены данные. Тип данных - string.")
        autorize()
    logfile = logfiles()
    logins = logfile[0]
    passwords = logfile[1]
    roles = logfile[2]
    i = 0
    autorization = False
    while i < len(logins):
        if logins[i] == login and passwords[i] == password:
            autorization = True
            role = roles[i]
            break
        i+=1
    if autorization:
        print("Авторизация успешна!")
        if role == "user":
            user(login)
        elif role == "admin":
            administrator(login)
    else:
        print("Неверный логин или пароль. Переводим вас в главное меню.")
        main()
def user(login : str):
    """
    Данная функция выполняет функции консольного меню, включающая в себя функции, доступные роли user.
    :param login: Логин пользователя, используемый для приветствия
    :return: Данная функция ничего не возвращает
    """
    while True:
        key = 0
        print(f"Здравствуйте, {login}!")
        try:
            key = int(input("Выберите действия:\n1. Вывести список товаров\n2. Выйти в меню\n3. Выйти из программы\n"))
        except:
            print("Неверный формат ввода. Нужен string.")
        if key == 1:
            spisok()
        elif key == 2:
            main()
        elif key == 3:
            sys.exit()
        else:
            print("Действие не найдено. Выберите либо 1 либо 2 либо 3.")
            user(login)
def administrator(login : str):
    """
    Данная функция выполняет функции консольного меню, включающая в себя функции, доступные роли admin.
    :param login: Логин пользователя, используемый для приветствия
    :return: Данная функция ничего не возвращает
    """
    while True:
        key = 0
        print(f"Здравствуйте, {login}!")
        try:
            key = int(input("Выберите действия:\n1. Вывести список товаров\n2. Редактирование товара\n3. Добавление товара\n4. Удаление товара\n5. Выйти в меню.\n6. Выйти из программы\n"))
        except:
            print("Неверный формат ввода. Нужен string.")
        if key == 1:
            spisok()
        elif key == 2:
            replace()
        elif key == 3:
            add()
        elif key == 4:
            delete()
        elif key == 5:
            main()
        elif key == 6:
            sys.exit()
        else:
            print("Действие не найдено. Выберите число в промежутке 1-6.")
            administrator(login)
def spisok():
    """
    Данная функция считывает файл товаров и выводит их с помощью таблицы tabulate.
    :return: Данная функция ничего не возвращает
    """
    print("Список товаров:")
    with open('tovar.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        headers = ["Наименование", "Описание", "Поставщик", "Цена", "Доступное кол-во"]
        print(tabulate(csv_reader, headers, tablefmt="grid"))
        file.close()
def replace():
    """
    Данная функция считывает файл для его дальнейшего изменения.
    :return:
    """
    where = 0
    lines = []
    try:
        with open('tovar.csv', 'r') as file:
            try:
                where = int(input("Введите номер строки товара, которого хотите заменить - "))
                if where < 1:
                    where = 1
            except:
                print("Неверный формат ввода. Нужен int.")
                replace()
            lines = file.readlines()
        file.close()
    except:
        print("Файл не заполнен или не существует.")
    change(lines, where)
def delete():
    """
    Данная функция удаляет выбранную пользователем строку из файла товаров.
    :return: Данная функция ничего не возвращает
    """
    where = 1
    try:
        where = int(input("Введите номер строки, которую хотите удалить - "))
        if where < 1:
            where = 1
    except:
        print("Неверный формат ввода. Нужен string.")
        delete()
    file = open('tovar.csv', 'r')
    lines = file.readlines()
    file.close()
    deletecontinue(lines, where)
def deletecontinue(lines : [str], where : int):
    """
    Данная функция удаляет строку, выбранную пользователем в прошлой функции.
    :param lines: Список строк файла
    :param where: Номер строки, которую необходимо удалить
    :return: Данная функция ничего не возвращает
    """
    lines[where - 1] = ""
    with open('tovar.csv', 'w') as file:
        i = 0
        while i < len(lines):
            file.write(lines[i])
            i+=1
    file.close()
def change(lines : [str], where : int):
    """
    Данная функция удаляет строку, выбранную пользователем в прошлой функции.
    :param lines: Список строк файла
    :param where: Номер строки, которую необходимо удалить
    :return: Данная функция ничего не возвращает
    """
    name = ""
    description = ""
    company = ""
    price = 0
    colichestvo = 0
    try:
        name = str(input("Введите наименование товара - "))
    except:
        print("Неверный формат ввода. Нужен str.")
        change(lines, where)
    try:
        description = str(input("Введите описание товара - "))
    except:
        print("Неверный формат ввода. Нужен str.")
        change(lines, where)
    try:
        company = str(input("Введите поставщика - "))
    except:
        print("Неверный формат ввода. Нужен str.")
        change(lines, where)
    try:
        price = int(input("Введите цену товара. Цена не может быть 0 или ниже - "))
        if price <= 0:
            print("Неверная цена. Мы разоримся.")
    except:
        print("Неверный формат ввода. Нужен int.")
        change(lines, where)
    try:
        colichestvo = int(input("Введите количество доступного товара на складе - "))
    except:
        print("Неверный формат ввода. Нужен int.")
        change(lines, where)
    lines[where - 1] = f"{name},{description},{company},{price},{colichestvo}"
    changes = open('tovar.csv', 'w')
    changes.writelines(lines)
    changes.close()
def add():
        """
        Данная функция добавляет товары по нескольким параметрам, введенным пользователем.
        :return: Данная функция ничего не возвращает
        """
        with open('tovar.csv', 'a') as file:
            try:
                name = str(input("Введите наименование товара - "))
            except:
                print("Неверный формат ввода. Нужен str.")
                add()
            try:
                description = str(input("Введите описание товара - "))
            except:
                print("Неверный формат ввода. Нужен str.")
                add()
            try:
                company = str(input("Введите поставщика - "))
            except:
                print("Неверный формат ввода. Нужен str.")
                add()
            try:
                price = int(input("Введите цену товара. Цена не может быть 0 или ниже - "))
                if price <= 0:
                    print("Неверная цена. Мы разоримся.")
            except:
                print("Неверный формат ввода. Нужен int.")
                add()
            try:
                colichestvo = int(input("Введите количество доступного товара на складе - "))
            except:
                print("Неверный формат ввода. Нужен int.")
                add()
            file.write(f"\n{name},{description},{company},{price},{colichestvo}")
            file.close()
if __name__ == main():
    main()