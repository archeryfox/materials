pal = input('введите слово палиндром: ')
i = 0
for s in pal:
    if pal[len(pal) - i - 1] == pal[i]:
        if i == len(pal)-1:
            print('это палиндром')
            break
    else:
        print('это не палиндром')
        break
    i += 1
