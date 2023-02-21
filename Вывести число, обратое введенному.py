try:
    chislo = int(input("Введите число: "))
    print(str(chislo)[::-1])
except ValueError:
    print("Вы ввели не число!\nПожалуйста, вводите только числа.")
