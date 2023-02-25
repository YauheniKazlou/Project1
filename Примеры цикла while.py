try:
    a = int(input("Ведите число натуральное число: "))
    if a <= 0:
        print("Вы ввели не натуральное число!")
    factorial = 1
    b = 1
    while b <= a:
        factorial *= b
        b += 1
    print("Факториал числа \"" + str(a)+"\" равен -", factorial)
except ValueError:
    print("Вы ввели не число!")
