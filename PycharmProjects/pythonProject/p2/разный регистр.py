stre = list(input('Ввести строку\n '))
i = 0
st = ''
for ch in stre:
    if i % 2 != 0:
        stre[i] = ch.upper()
    else:
        stre[i] = ch.lower()
    st += stre[i]
    i += 1
print(st)
