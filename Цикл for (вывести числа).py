try:
    min1 = int(input("Введите минимум: "))
    max1 = int(input("Введите максиммум: "))
    if max1 < min1:
        print("Максимум не может быть меньше минимума!")
    step = int(input("Введите шаг: "))
except ValueError:
    print("Вводите только числа!")
for i in range(int(min1), int(max1) + 1, int(step)):
    print(i)
