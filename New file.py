

try:
    chislo1 = input("Введите сегодняшний день недели: ")
    chislo2 = input("Введите сегодняшнее число: ")
    print("Сегодня: " + chislo1 + " " + int(chislo2) + "-го")
except TypeError:
    print("Используются разные типы данных в функции!")
except ValueError:
    print("Введена строка вместо цифр!")