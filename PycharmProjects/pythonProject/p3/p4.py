listin = []
inputing = int(input('Введите цифру: '))
listin.append(inputing)
if listin[0] == 0:
    print("Вы завершили программу раньше чем ввели что-нибудь...")
while inputing != 0:
    inputing = int(input('Введите цифру: '))
    listin.append(inputing)
    if inputing == 0:
        listin.remove(0)
        listin.sort()
        str = ''
        for i in listin:
            if i == listin[len(listin)-1]:
                str += f'{i}'
            else:
                str += f'{i}, '
        print(str)
