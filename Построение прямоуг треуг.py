a = int(input("Введите высоту треугольника: "))
for i in range(1, a + 1):
    for b in range(1, i + 1):
        print("|__", end="")
    print()
