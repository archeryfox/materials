def main():
     try:
          num = [14,20, 35, 80]


          first = int(input("Напишите любое целое число: "))
          second = int(input("Введите еще одно число: "))
          # third = int(input("Введете число"))
          print(first/second)
          i = int(input("Введите номер в массиве для вывода числа из него"))
          num[i]
          print(num[i])
          print ("Введите число а затем слово для ошибки с смешиванием переменных")
          a = int(input("число:"))
          b = str(input("Слово"))
          print(a+b)
          print(i_am_here)
     except TypeError:
          print("Смешивание переменных разных типов")
     except NameError:
          print("Переменная i_am_here не существует")
     except IndexError:
          print("Ошибка неверна поиция в массиве (отсутствует число в этой ячейке)")
     except ZeroDivisionError:
          print("Разделить число на ноль - невозможно!")

     except ValueError:
          print("Неправильный тип переменной")

     finally:
          print("Работа программы завершена")
# def moretrables():
#      a = 5
#      b = 4
#      с = a b
#      except SyntaxError:
#           print("Вы не сделали операцию с переменными")
#      except IndentationError:
#           print("Ошибка отспупа")
#      finally:
#           print("dfsdf")
def more():
     try:
          a = {1: 'a', 2: 'b', 3: 'c'}
          print(a[5])
     except LookupError:
          print("Исключение KeyError.")
     else:
          print(f"Программа решена без проблем")


def onemoretime():
     try:
          a = 100
          b = "PythonRu"
          assert a == b
     except AssertionError:
          print("Исключение AssertionError.")
     else:
          print("Успех, нет ошибок!")

def overflow():
     try:
          import math
          print(math.exp(1000))
     except OverflowError:
          print("Исключение OverFlow.")
     else:
          print("Успех, нет ошибок!")
print(overflow())