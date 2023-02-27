try:
    a = int(input("Введите натуральное число: "))
    if a <= 0:
        print("Вводить необходимо только натуральные числа!")
    print("Совершенные числа в диапазоне от 1 до " + str(a) + " равны:")
    for i in range(1, a + 1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if s == i:
            print(i)
except ValueError:
    print("Вводите только числа!")
