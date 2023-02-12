import csv
import sys
from tabulate import tabulate

isnext = False

class Authorisation:
    '''
    Класс, содержащий методы  пользователя
    '''

    @staticmethod
    def LoginFiles() -> list:
        """
        Метод читает вводимые логины, пароли, роли
        :return: Список логинов, паролей и ролей пользователей.
        """
        logs = []
        passwords = []
        roles = []
        with open("user.csv") as file:
            rdr = csv.reader(file, delimiter=',')
            next(rdr)
            for read in rdr:
                logs.append(read[0])
                passwords.append(read[1])
                roles.append(read[2])
        file.close()
        return [logs, passwords, roles]

    @staticmethod
    def AuthorizationEvent() -> None:
        """
        Данный метод служит входом в систему для уже зарегистрированных пользователей. В случае удачной регистрации
        входящего переносит в функцию user или Administrator, в зависимости от его роли.
        """
        AuthLogin = ""
        AuthPassword = ""
        AuthRole = ""
        try:
            AuthLogin = input("Авторизация. Введите ваш логин: ")
        except:
            print("povtori")
            Authorisation.AuthorizationEvent()
        try:
            AuthPassword = input("Введите ваш пароль: ")
        except:
            print("Try one more time")
            Authorisation.AuthorizationEvent()
        LoginFile = Authorisation.LoginFiles()
        Logs = LoginFile[0]
        Passwords = LoginFile[1]
        Roles = LoginFile[2]
        i = 0
        AutorizationMarker = False
        while i < len(Logs):
            if Logs[i] == AuthLogin and Passwords[i] == AuthPassword:
                AutorizationMarker = True
                AuthRole = Roles[i]
                break
            i += 1
        if AutorizationMarker:
            print("Принято, добро пожаловать в систему дорогой пользователь")
            if AuthRole == "user":
                User.user(AuthLogin)
            elif AuthRole == "admin":
                Admin.Administrator(AuthLogin)
        else:
            print("Неверный логин или пароль. Переводим вас в главное меню.")
            main()


class Registration:
    @staticmethod
    def RegistrationEvent() -> None:
        """
        Данная функция проводит регистрацию пользователя, прося его логин и повторение пароля. В случае занятого логина,
        пользователя переводит в поле авторизации, в случае неверного повторения пароля - в регистрацию. После,
        функция вызывает доп.функцию regcontinue, которая записывает логин и пароль в базу данных пользователей.
        """
        RegisterLogin = ""
        try:
            RegisterLogin = input("Введите желаемый логин - ")
        except:
            print("Ошибка. Попробуйте еще раз. Тип данных - string.")
            Registration.RegistrationEvent()
        LoginFile = User.LoginFiles()
        logs = LoginFile[0]
        loginexist = RegisterLogin in logs
        if loginexist:
            print("Логин уже занят. Переводим вас в поле авторизации.")
            Authorisation.AuthorizationEvent()
        try:
            RegisterPassword = input("Введите желаемый пароль - ")
            if RegisterPassword != input("Повторите пароль - "):
                print("Неверно повторен пароль.")
                Registration.RegistrationEvent()
            else:
                Registration.PostRegistration(RegisterLogin, RegisterPassword)
        except:
            print("Ошибка. Попробуйте еще раз. Тип данных - string.")
            Registration.RegistrationEvent()

    @staticmethod
    def PostRegistration(RegisterLogin: str, RegisterPassword: str) -> None:
        """
        Данная функция записывает данные пользователя в файл.
        :param RegisterLogin: Логин, введнный пользователем
        :param RegisterPassword: Пароль, введенный пользователем
        """
        with open("user.csv", "a") as file:
            file.write(f"\n{RegisterLogin},{RegisterPassword},user")
        file.close()
        print("Регистрация завершена. Ваши данные в сохранности лежат в Csvшке")
        main()


class Admin:
    '''
    Класс, в котором содержится весь функционал для админинистрирования
    '''

    @staticmethod
    def change(lines: [str], marker: int) -> None:
        """
        Данная функция удаляет строку, выбранную пользователем в прошлой функции.
        :param lines: Список строк файла
        :param marker: Номер строки, которую необходимо удалить
        """
        Name = ""
        Description = ""
        Company = ""
        Price = 0
        Count = 0
        try:
            Name = str(input("Введите наименование товара - "))
        except:
            print("Неверный формат ввода. Нужен str.")
            Admin.change(lines, marker)
        try:
            Description = str(input("Введите описание товара - "))
        except:
            print("Неверный формат ввода. Нужен str.")
            Admin.change(lines, marker)
        try:
            Company = str(input("Введите поставщика - "))
        except:
            print("Неверный формат ввода. Нужен str.")
            Admin.change(lines, marker)
        try:
            Price = int(input("Введите цену товара. Цена не может быть 0 или ниже - "))
            if Price <= 0:
                print("Неверная цена. Мы разоримся.")
        except:
            print("Неверный формат ввода. Нужен int.")
            Admin.change(lines, marker)
        try:
            Count = int(input("Введите количество доступного товара на складе - "))
        except:
            print("Неверный формат ввода. Нужен int.")
            Admin.change(lines, marker)
        lines[marker - 1] = f"{Name},{Description},{Company},{Price},{Count}"
        changes = open('tovar.csv', 'w')
        changes.writelines(lines)
        changes.close()

    @staticmethod
    def Deleting():
        """
        Данная функция удаляет выбранную пользователем строку из файла товаров.
        """
        marker = 1
        try:
            marker = int(input("Введите номер строки, которую хотите удалить - "))
            if marker < 1:
                marker = 1
        except:
            print("Неверный формат ввода. Нужен string.")
            Admin.Deleting()
        file = open('tovar.csv', 'r')
        lines = file.readlines()
        file.close()
        Admin.PostDeleting(lines, marker)

    @staticmethod
    def PostDeleting(lines: [str], marker: int) -> None:
        """
        Данная функция удаляет строку, выбранную пользователем в прошлой функции.
        :param lines: Список строк файла
        :param marker: Номер строки, которую необходимо удалить
        """
        lines[marker - 1] = ""
        with open('tovar.csv', 'w') as file:
            i = 0
            while i < len(lines):
                file.write(lines[i])
                i += 1
        file.close()

    @staticmethod
    def Administrator(login: str) -> None:
        """
        Метод выполняет действия консольного меню, включающая в себя функционал, роли admin.
        :param login: Логин пользователя, используемый для приветствия
        """
        while True:
            key = 0
            print(f"Здравствуйте, дорогой {login}!")
            try:
                key = int(input(
                    "Выберите действия:\n"
                    "1 - Вывести список товаров\n"
                    "2 - Редактирование товара\n"
                    "3 - Добавление товара\n"
                    "4 - Удаление товара\n"
                    "5 - Выйти в меню.\n"
                    "6 - Выйти из программы\n"))
            except:
                print("Повторите ввод.....")
            if key == 1:
                Admin.Listing()
            elif key == 2:
                Admin.Refactoring()
            elif key == 3:
                Admin.Add()
            elif key == 4:
                Admin.Deleting()
            elif key == 5:
                main()
            elif key == 6:
                sys.exit()
            else:
                print("Действие не найдено. Выберите число в промежутке 1-6.")
                Admin.Administrator(login)

    @staticmethod
    def Add():
        """
        Данная функция добавляет товары по нескольким параметрам, введенным пользователем.
        """
        with open('items.csv', 'a') as file:
            try:
                Name = str(input("Введите название: "))
            except:
                print("Мдаа, чот неправильно")
                Admin.Add()
            try:
                Description = str(input("Введите описание:"))
            except:
                print("Чот нули лишние невидимые....")
                Admin.Add()
            try:
                Company = str(input("Введите поставщика - "))
            except:
                print("")
                Admin.Add()
            try:
                Price = int(input("Введите цену товара. Цена не может быть 0 или ниже - "))
                if Price <= 0:
                    print("Неверная цена. Мы разоримся.")
            except:
                print("Неверный формат ввода. Нужен int.")
                Admin.Add()
            try:
                count = int(input("Введите количество доступного товара на складе - "))
            except:
                print("Введите цифру.")
                Admin.Add()
            file.write(f"\n{Name},{Description},{Company},{Price},{count}")
            file.close()

    @staticmethod
    def Listing() -> None:
        """
        Метод считывает файл товаров и выводит их в tabulate.
        """
        print("Список товаров:")
        with open('items.csv', 'r') as file:
            rdr = csv.reader(file, delimiter=',')
            print(tabulate(rdr, headers=["Название", "Описание", "Поставщик", "Цена", "Количество товара"], tablefmt="pipe"))
            file.close()

    @staticmethod
    def Refactoring() -> None:
        """
        Данная функция считывает файл для его дальнейшего изменения.
        """
        marker = 0
        lines = []
        try:
            with open('items.csv', 'r') as file:
                try:
                    marker = int(input("Введите номер товара, которого хотите заменить - "))
                    if marker < 1:
                        marker = 1
                except:
                    print("Неверный формат ввода. Нужен int.")
                    Admin.Refactoring()
                lines = file.readlines()
            file.close()
        except:
            print("Файл не заполнен или не существует.")
        Admin.change(lines, marker)


class User:
    """
    Класс взаимодействия пользователя,
    """

    @staticmethod
    def user(login: str) -> None:
        """
        Метод взаимодействия пользователя
        :param login: Логин пользователя
        """
        while True:
            key = 0
            print(f"Здравствуйте, {login}!")
            try:
                key = int(
                    input("Выберите действия:"
                          "\n1. Вывести список товаров"
                          "\n2. Выйти в меню"
                          "\n3. Выйти из программы\n"))
            except:
                print("Неверный формат ввода. Нужен string.")
            if key == 1:
                Admin.Listing()
            elif key == 2:
                main()
            elif key == 3:
                sys.exit()
            else:
                print("Повторите ввод")
                User.user(login)

    @staticmethod
    def LoginFiles():
        """
        Данный метод считывает логины, пароли и роли пользователей и возвращает их.
        :return: Логины, пароли, роли
        """
        logs = list()
        passwords = list()
        roles = list()
        with open("user.csv") as fs:
            rdr = csv.reader(fs, delimiter=',')
            next(rdr)
            for read in rdr:
                logs.append(read[0])
                passwords.append(read[1])
                roles.append(read[2])
        fs.close()
        return [logs, passwords, roles]


def main():
    """
    Точка входа пользователя
    """
    print('──────▄▀▄─────▄▀▄\n'+
          '─────▄█░░▀▀▀▀▀░░█▄\n'+
          '─▄▄──█░░░░░░░░░░░█──▄▄\n'+
          '█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█')
    while True:
        Choise = ""
        try:
            Choise = int(input("Это электронная система магазина Crякос\n"
                               "1 - Регистрация\n"
                               "2 - Войти по логину\n"
                               "3 - Закрыть соединение\n"))
        except:
            print("Некорректный ввод! Повторите")
            main()
        if Choise == 1:
            Registration.RegistrationEvent()
        elif Choise == 2:
            Authorisation.AuthorizationEvent()
        elif Choise == 3:
            sys.exit()
        else:
            print("Повторите..")
            main()


main()
