'''
2. Дано целое число. Если оно является положительным, то прибавить к
нему 1; если отрицательным, то вычесть из него 2; если нулевым, то
заменить его на 10. Вывести полученное число.
'''

# ввод числа
a = int(input('Введите число: '))
if a > 0:
# если введёно положительное, то выведем инкриментированное число
    print(a+1)
elif a < 0:
    print(a-2)
# если введено отрицательное, то вывести уменьшенное на 2 число
else:
    a = 10
    print(a)
# иначе просто заменим введённые данны