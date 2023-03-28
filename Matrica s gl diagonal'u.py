n = int(input("Введите колличество строк и столбцов: "))
A = [1] * n
print(A)
for i in range(n):
    A[i] = ["*"] * n
    print(A[i])
for i in range(n):
    for j in range(n):
        if i < j:
            A[i][j] = 0
        elif i > j:
            A[i][j] = 2
        else:
            A[i][j] = 1
    print(A[i])


print("\nВторой способ решения этой задачи:")
A = [0] * n
for i in range(n):
    A[i] = [0] * n
for i in range(n):
    A[i][i] = 1
for i in range(n):
    for j in range(i + 1, n):
        A[i][j] = 0
for i in range(n):
    for j in range(0, i):
        A[i][j] = 2
    print(A[i])