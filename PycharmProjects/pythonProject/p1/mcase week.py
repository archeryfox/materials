'''
Дано целое число в диапазоне 1–7. Вывести строку — название дня
недели, соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.).
'''
# Ввод номера дня недели
d = int(input('Номер дня недели '))

# Вывод дня недели в зависимости от введённого номера
match d:
    case 1: print("Понедельник")
    case 2:
        print("Вторник")
    case 3:
        print("Среда")
    case 4:
        print("Четверг")
    case 5:
        print("Пятница")
    case 6:
        print("Суббота")
    case 7:
        print("Воскресенье")