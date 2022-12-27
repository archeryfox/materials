from tabulate import tabulate

class Product:
    def __init__(self, count, price, unit_weight):
        self.__Price = price
        self.__Weight = unit_weight
        self.__Count = count

    def getUnitWeight(self):
        """

        :return: возвращает self.__Weight
        """
        return self.__Weight

    def getQuantity(self):
        """

        :return: возвращает self.__Count
        """
        return self.__Count

    def getPrice(self):
        """

        :return: возвращает self.__Price
        """
        return self.__Price

    def SortInfo(self, name, price):
        """

        :param name: Название нашего товара
        :param price: Полная цена внутри контейнера
        """
        Result.append((name, self, price))

    def __lt__(self, other):
        """


        :param other: берёт параметр из нашей переменной к которой мы прописали .sort()
        :return: возвращает True или False, для сравнения и сортировки списка
        """
        return self.__Weight < other.__Weight

    def showInfo(self):
        """
        Вывод результата
        """
        Result.sort()
        TimesResult[0] = [str(self.__Count)]
        TimesResult[1] = [str(self.__Price)]
        TimesResult[2] = [str(self.__Weight)]


TimesResult = ["Кол-во", "Цена", "Вес одного", "Цена груза в контейнере"]
Result = []
ban = ''
# создаём экземпляр с параметрами товаров которые нам нужны
cola = Product(1254, 120, 0.35)
Table = Product(239, 7023, 16)
pc = Product(73, 50000, 10)
car = Product(8, 2000000, 1328)
Volume = 2200
# Создаём список экзепляров
Warehouse = [cola, Table, pc, car]
# Название товаров
NameWarehouse = ["cola", "Table", "pc", "car"]
# Цикл по размеру переменной Warehouse, в которой мы высчитываем стоимость и кол-во товаров, которые вместяться в
# контейнер, сортируем через if elif else по разным параметрам товара
for i in range(len(Warehouse)):
    x = Volume // Warehouse[i].getUnitWeight()
    if x > Warehouse[i].getQuantity():
        y = Warehouse[i].getPrice() * Warehouse[i].getQuantity()
        Warehouse[i].SortInfo(NameWarehouse[i], y)
    elif x < 1:
        print("Товар", Warehouse[i], "не вместился")
    else:
        Warehouse[i].SortInfo(NameWarehouse[i], x * Warehouse[i].getPrice())
m = 0
# Цикл для вывода результатов
for i in Result:
    i[1].showInfo()
    TimesResult[3] = [str(i[2])]
    print(tabulate(TimesResult, headers=[NameWarehouse[m]], tablefmt='psql', stralign='center'), "\n")
    for n in TimesResult:
        ban += ''.join(n)

    f = open('xyz.txt', 'a+')
    f.write(NameWarehouse[m] + " : " + ban + '\n')
    f.close()
    m += 1

