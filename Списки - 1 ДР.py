try:
    a = int(input("Введите отрицательное число начала списка: "))
    if a >= 0:
        print("Число должно быть отрицательным!")
    b = int(input("Введите положительное число окончания списка: "))
    if b <= 0:
        print("Число должно быть положительным!")
except ValueError:
    print("Вводить необходимо только числа!")
chisla = list(range(a, b+1))
print(chisla)
s = 0
for i in chisla:
    if i > 0:
        if i % 2 == 0:
            s += i
print("Сумма положительных четных чисел равна", s)
