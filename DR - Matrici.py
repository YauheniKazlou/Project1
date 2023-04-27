import random
a = int(input("Введите коллличество строк и столбцов: "))
A = ["*"] * a
print("Первое действие -", A)
for i in range(a):
    A[i] = [1] * a
    print(A[i])
for i in range(a):
    for j in range(a):
        A[i][j] = random.randrange(-100, 100)
    print(A[i])

S1 = 0
A1 = []
for i in range(a):
    for j in range(a):
        if i == j:
            S1 += A[i][j]
        elif i > j:
            if A[i][j] < 0:
                A1.append(A[i][j])
print("Сумма элементов главной диагонали равна ", S1)
print("Колличество отрицательных чисел, расположенных ниже гл. диагонали равно -", len(A1))


