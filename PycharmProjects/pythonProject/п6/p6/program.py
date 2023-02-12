import csv
import sys
from tabulate import tabulate
from adding import REDACT
add = REDACT()

class Program:
    '''
    Runtime
    '''
    def Main(self) -> None:
        """
        Метод для выбора действия и следующего вызова метода и представлены как консольные рационы.\n
        Эта функция работает до тех пор, пока пользователь не выйдет.
        """
        while True:
            key = 0
            try:
                key = int(input(
                    "Выберите действие:"
                    "\n 1 - Добавить заявку"
                    "\n 2 - Вывести отсортированный список заявок по марке"
                    "\n 3 - Вывести отсортированный список заявок по неисправности"
                    "\n 4 - Закрыть программу\n"))
            except:
                print("Неверный формат ввода. Попробуйте ещё раз. Нужен формат int.")
                Program.Main(self)
            if key == 1:
                add.Redact()
            elif key == 2:
                sort(True)
            elif key == 3:
                sort(False)
            elif key == 4:
                sys.exit()
            else:
                print("Действие не найдено. Введите номер действия снова.")


def sort(Marked : bool):
    """
    Метод принимает bool, чтобы в замисимости от фактора, отсортировать
    :param Marked: В зависимости от значения сортируется список
    """
    with open('cars.csv', 'r') as fstream:
        Reader = csv.reader(fstream, delimiter=',')
        next(Reader)
        if Marked:
            print("Список, отсортированный по марке")
            sortTuple = sorted(Reader, key=lambda x: x[-3])
        else:
            print("Список, отсортированный по неисправности")
            sortTuple = sorted(Reader, key=lambda x: x[-1])
        print(tabulate(sortTuple, ["Марка", "Номер", "Неисправность"], tablefmt="pipe"))
        fstream.close()
    p = Program()
    p.Main()

while True:
    p = Program()
    Program.Main(self=p)