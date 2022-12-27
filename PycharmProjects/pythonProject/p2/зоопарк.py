group = int(input("Сколько вас? "))
ticket = 0.0
every = 0
for every in range(group):
    age = int(input("Сколько тебе лет? - "))
    if age <= 3:
        pass
    if age > 3 and age <= 12:
        ticket += 14
    if age >= 65:
        ticket += 18
    else: ticket += 23
print(f'С вас {ticket:.{2}f}$')
