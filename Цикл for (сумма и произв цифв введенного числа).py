try:
    chislo = input("Введите натуральное трехзначное число: ")
    if len(chislo) != 3:
        print("Число", "\"" + chislo + "\"", "не является натуральным трехзначным!")
except ValueError:
    print("Введите только цифры")

print("Сумма цифр числа", "\"" + chislo + "\"", "равна -", int(chislo[0]) + int(chislo[1]) + int(chislo[2]))
print("Произведение цифр числа", "\"" + chislo + "\"", "равно -", int(chislo[0]) * int(chislo[1]) * int(chislo[2]))
