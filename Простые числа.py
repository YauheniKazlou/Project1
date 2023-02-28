a = int(input("Введите диапазон простых чисел: "))
print("Простые числа в диапазоне от 1 до", str(a) + ":")
for i in range(1, a + 1):
    summ = 0
    for j in range(1, i + 1):
        if i % j == 0:
            summ += j
        if summ == int(i) + 1:
            print(i, end='\t')
