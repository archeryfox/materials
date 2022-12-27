i = 0
ino = 0
first = True
b = int(input('Введите цифру: '))
if b == 0 and first:
    print("Ошибка")
while b != 0:
    i += 1
    first = False
    ino += b
    b = int(input('Введите цифру: '))

print(f"Сренее - {ino/i}")
if b == 0 and not first:
    print("Выход...")
