'''
4. Разработайте программу, запрашивающую у пользователя букву латинского алфавита.
Если введенная буква входит в следующий список (a, e, i, o или u), необходимо вывести сообщение о том,
что эта буква гласная. Если была введена буква y, программа должна написать,
что эта буква может быть как гласной, так и согласной. Во всех других случаях должно выводиться сообщение о том,
что введена согласная буква
'''

# Ввод
s = input('Введите букву - ')
if s == 'a' \
    or s == 'e' \
    or s == 'i' \
    or s == 'o' \
    or s == 'u':
    print('это гласная')

# вывести исключение для "y"
elif s == 'y':
    print('эта буква может быть как гласной, так и согласной')

# все остальные символы
else:
    print('это согласная')