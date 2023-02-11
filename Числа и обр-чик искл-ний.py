try:
    chislo = input("Введите число: ")
    if len(chislo) != 3:
        print("Вы ввели не трехзначное число!")
    print(int(chislo[0]) + int(chislo[1]) + int(chislo[2]))
except ValueError:
    print("Вводить можно только цифры!")
