import csv
from tabulate import tabulate
"""
Имеется N типов товаров (названия известны). Для каждого товара задано количество
единиц этого товара, цена и вес единиц товара. Требуется загрузить контейнер (не
превышая его известной грузоподъемности) товарами одного типа так, чтобы стоимость
груза в контейнере была максимальной. Выполнить сортировку списка.
"""
import random
class Unit:
    def __init__(self, type, price, weigh, count):
        self.type = type
        self.price = price
        self.weigh = weigh
        self.count = count
    @classmethod
    def setWeigh(cls):
        weigh = 0
        try:
            weigh = int(input('Введите вес товара: '))
            if weigh < 0:
                print('Типо подлетают и поднимают бокс?..')
                Unit.setWeigh()
            if weigh == 0:
                print('Нельзя ничего не весить...')
                Unit.setWeigh()
        except:
            print('Некоректно, повторите')
            Unit.setPrice()
        return weigh

    @classmethod
    def setPrice(self):
        price = 0
        try:
            price = int(input("Введите цену товара: "))
            if price <= 0:
                print('Мы обеднеем..')
                self.setPrice()
        except:
            print('Некоректно, повторите')
            self.setPrice()
        return price

    @classmethod
    def setCount(cls):
        count = 0
        try:
            count = int(input('Введите количество товаров: '))
            if count <= 0:
                print('Мы обеднеем..')
                Unit.setCount()
        except:
            print('Некоректно, повторите')

            Unit.setCount()
        return count


class Container:
    @classmethod
    def Initing(cls) -> None:
        '''
        Сериализация
        '''
        Container.StCon = Container(Container.setVolume())
        SomeUnit = Unit(input('Введите название товара: '), Unit.setPrice(), Unit.setWeigh(), Unit.setCount())
        with open("tbl.csv", 'a', newline='') as fist:
            wrtr = csv.writer(fist)
            wrtr.writerow([SomeUnit.type, SomeUnit.price, SomeUnit.weigh, SomeUnit.count])
        fist.close()
    @staticmethod
    def Import(cls,i=0):
        """
        Десериализация
        """
        with open("tbl.csv", 'r') as fist:
            redr = csv.reader(fist, delimiter=',')
            next(redr)
            listProds = list(redr)
            if i==1:
                listProds = sorted(listProds, reverse=True, key=lambda x: x[0])
                print('Сортировано по названию')
                print(
                    tabulate(listProds,
                             tablefmt='grid', headers=["Название", "Цена", "Вес", "Количество"], showindex=True)
                )
            if i == 2:
                listProds = sorted(listProds, reverse=True, key=lambda x: x[-1])
                # print('Сортировано по весу')
                # print(
                #     tabulate(listProds,
                #              tablefmt='grid', headers=["Название", "Цена", "Вес", "Количество"], showindex=True)
                # )
            if i == 0:
                return listProds
        fist.close()
        return listProds

    AllConteiner = list()
    def __init__(self,vol):
        self.volume = vol
        '''
        Ёмкость
        '''
        self.price = 0

    def Counter(self):
         i = 0
         i2 = 0
         '''
         счётчик цикла
         '''
         memVol = self.volume
         products = Container.Import(Container,2)
         for dlist in products:
             i2+=1
             prod2 = Unit(dlist[0], int(dlist[1]), int(dlist[2]), int(dlist[3]))
             # print(str(prod2.weigh) +' gr')
             while self.volume > 0:
                 i += 1
                 self.volume -= prod2.weigh * i
                 self.price += prod2.price * i
             # print(prod2.type)
             # print(f'{self.price} руб')
             # print(str(memVol - prod2.weigh * (i-1))+' кг')
             # print()
             i = 0

         # with open('container.csv', "r") as file:
         #     redr = csv.reader(file, delimiter=',')
         #     next(redr)
         #     list1= list(redr)
         #     list1 = sorted(list1, key=lambda x:[-1])
         #     print(
         #         tabulate(list1,
         #                  tablefmt='grid', headers=["Вес", "Цена"])
         #     )
         # file.close()

    @classmethod
    def setVolume(cls):
        volume = 0
        try:
            volume = int(input('Введите объём контейнера: '))
            if volume < 0:
                print('Типо чёрная дыра?..')
                Container.setVolume()
            if volume == 0:
                print('Тогда нет бокса...')
                Container.setVolume()
        except:
            print('Некоректно, повторите')
            Unit.setPrice()
        return volume


# добавить товары
# показать товары сорт
# закрыть
#
#
# pens = Unit('ручки', 100,15,10*30)
# phones = Unit('айфоны',60_000,293,20)
# apples = Unit('яблоки', 4000,373*10,30)
# # рандомная вместимость
#
# print(container.volume)
# memVol = container.volume
# print()
# products = [pens,phones,apples]
#
# i=0
# '''
# счётчик цикла
# '''
# memVol2 = container.volume
# for prod in products:
#     print(str(prod.weigh) +' gr')
#     while container.volume > 0:
#         i += 1
#         container.volume -= prod.weigh * i
#         container.price += prod.price * i
#     print(prod.type)
#     print(f'{container.price} руб')
#     print(str(memVol - prod.weigh * (i-1))+' кг')
#     print()
#     i = 0
#     container.volume= memVol
#     container.price = 0
# print(memVol2)
StCon = Container(4000)
def Start():

    while True:
        i = 0
        try:
            i = int(input('Что вы хотите?\n 1 - Запуск\n 2 - Сортировка по названию\n 3 - Cортировка по весу\n'))
        except:
            Start()
        match(i):
            case 1:
                Container.Initing()
            case 2:
                Container.Import(Container,1)
            case 3:
                StCon.Counter()

Start()