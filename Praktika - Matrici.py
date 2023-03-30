import random
A = []
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
for i in range(n):
    A1 = []
    for j in range(m):
        A1.append(random.randint(-100, 100))
    A.append(A1)
print("\nMатрица:")
for i in A:
    print(i)
print()
for i in A:
    print("Сумма чисел", int(A.index(i)), "строки равна:", sum(i))
