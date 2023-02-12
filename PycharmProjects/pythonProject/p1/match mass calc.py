# Выбор вида единиц массы
var = int(input(' 1 - кг\n 2 - мг\n 3 - г\n 4 - т\n 5 - ц \n Выберите номер единицы массы '))

# Ввод количества массы
mass = int(input('Введите массу '))

# Вывод переведённых единиц массы
match var:
    case 1:
        print(mass,' кг')
    case 2:
        print(mass/10000,'кг')
    case 3:
        print(mass/1000,'кг')
    case 4:
        print(mass*1000,'кг')
    case 5:
        print(f'{mass*100} кг')