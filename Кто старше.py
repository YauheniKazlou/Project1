name1 = input("Введите имя первого человека: ")
a = int(input("Введите год рождения первого человека: "))
if int(a) < 0:
    print("Дата не может быть отрицательным числом!")
b = int(input("Введите месяц рождения первого человека: "))
if int(b) <= 0:
    print("Дата не может быть отрицательным числом или равна нулю!")
elif int(b) > 12:
    print("Число месяца не может быть больше 12!")
c = int(input("Введите день рождения первого человека: "))
if int(c) <= 0:
    print("Дата не может быть отрицательным числом или равна нулю!")
elif int(c) > 31:
    print("Число дня месяца не может быть больше 31!")

name2 = input("Введите имя второго человека: ")
a1 = int(input("Введите год рождения второго человека: "))
if int(a1) < 0:
    print("Дата не может быть отрицательным числом!")
b1 = int(input("Введите месяц рождения второго человека: "))
if int(b1) <= 0:
    print("Дата не может быть отрицательным числом или равна нулю!")
elif int(b1) > 12:
    print("Число месяца не может быть больше 12!")
c1 = int(input("Введите день рождения второго человека: "))
if int(c1) <= 0:
    print("Дата не может быть отрицательным числом или равна нулю!")
elif int(c1) > 31:
    print("Число месяца не может быть больше 31!")

if a < a1:
    print(str.capitalize(name1), "старше, чем", str.capitalize(name2))
if a1 < a:
    print(str.capitalize(name2), "старше, чем", str.capitalize(name1))
if a == a1:
    if b > b1:
        print(str.capitalize(name1), "старше, чем", str.capitalize(name2))
    if b1 > b:
        print(str.capitalize(name2), "старше, чем", str.capitalize(name1))
    if b == b1:
        if c > c1:
            print(str.capitalize(name1), "старше, чем", str.capitalize(name2))
        if c1 > c:
            print(str.capitalize(name2), "старше, чем", str.capitalize(name1))
        else:
            print(str.capitalize(name1), "и", str.capitalize(name2), "одного возраста.")
