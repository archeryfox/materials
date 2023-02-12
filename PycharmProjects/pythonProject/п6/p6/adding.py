from tabulate import tabulate
import csv

class REDACT:
    '''
    Класс отвечающий за добавление и сортировку таблицы
    '''
    def Redact(self) -> None:
        '''
        Метод просит пользователя ввести количество машин и отправляет данные методу Redact вместе с 0 в качестве счетчика цикла
        '''
        try:
            Couple = int(input("Введите количество машин - "))
            REDACT.Redacting(self, 0, Couple)
        except:
            print("Неверный формат ввода. Попробуйте еще раз. Нужен формат int.")
            REDACT.Redact(self)

    def Redacting(self, i: int, Couple: int) -> None:
        '''
        Метод просит пользователя вводить данные о заявке, количество запросов этих данных зависит
        от введенного пользователем количества машин
        :param i: Счетчик цикла
        :param Couple: Количество машин, полученное от пользователя
        '''
        while i < Couple:
            with open('cars.csv', 'a') as fstream:
                try:
                    wrong = input("Введите неисправность вашей машины - ")
                except:
                    print("Неверный формат ввода. Нужен str.")
                    REDACT.Redact(i, Couple)
                try:
                    number = input("Введите номер вашей машины - ")

                except:
                    print("Неверный формат ввода. Нужен str.")
                    REDACT.Redact(i, Couple)
                try:
                    Markeda = input("Введите марку вашей машины - ")
                    '''
                    Марка автомобиля
                    '''
                except:
                    print("Неверный формат ввода. Нужен str.")
                    REDACT.Redact(i, Couple)
                fstream.write(f"\n{Markeda},{number},{wrong}")
                i += 1
                fstream.close()

    def sort(self, Marked: bool):
        """
        Метод принимает значение типа данных bool, с помощью которого определяет, каким образом отсортировать и вывести список заявок.
        :param Marked: В зависимости от значения сортируется список
        """
        with open('cars.csv', 'r') as fstream:
            csv_reader = csv.reader(fstream, delimiter=',')
            next(csv_reader)
            if Marked:
                print("Список, отсортированный по марке")
                SortTuple = sorted(csv_reader, key=lambda x: x[-1])
            else:
                print("Список, отсортированный по неисправности")
                SortTuple = sorted(csv_reader, key=lambda x: x[-3])
            print(tabulate(SortTuple, ["Марка", "Номер", "Неисправность"], tablefmt="grid"))
            fstream.close()
