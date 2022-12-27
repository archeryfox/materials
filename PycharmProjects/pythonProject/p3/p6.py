listin = [ [],[],[] ]
inputing = input('Введите цифру: ')
stry = ''
if inputing == '':
    print("Вы завершили программу раньше чем ввели что-нибудь...")
elif int(inputing) < 0:
    listin[0].append(int(inputing))
elif int(inputing) == 0:
    listin[1].append(int(inputing))
elif int(inputing) > 0:
    listin[2].append(int(inputing))
while inputing != '':
    inputing = input('Введите цифру: ')
    if inputing == '':
        for i in listin:
                    for j in i:
                        stry += f'{j}, '
    elif int(inputing) < 0:
        listin[0].append(int(inputing))
    elif int(inputing) == 0:
        listin[1].append(int(inputing))
    elif int(inputing) > 0:
        listin[2].append(int(inputing))
stry = stry[:-2]
print(stry)
