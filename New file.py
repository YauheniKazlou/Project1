try:
    chislo1 = input("Введите сегодняшний день недели: ")
    chislo2 = input("Введите сегодняшнее число: ")
    print("Сегодня:", str.capitalize(chislo1), chislo2 + "-го")
except ValueError:
    print("Введена строка вместо цифр!")
try:
    chislo1 = input("Введите первое число: ")
    chislo2 = input("Введите второе число: ")
    print("Результат:" + int(chislo1) + int(chislo2))
except TypeError:
    print("Используются разные типы данных в функции!")