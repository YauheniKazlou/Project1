n = int(input("Введите колличество строк и столбцов: "))
A = []
for i in range(n):
    for j in range(n):
        if i < j:
            A[i][j] = 0
        elif i > j:
            A[i][j] = 2
        else:
            A[i][j] = 1
print(A)
