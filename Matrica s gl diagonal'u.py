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

# Второй способ решения этой задачи
n = int(input("Введите колличество строк и столбцов: "))
A = []
for i in range(n):
    A[i][i] = 1
for i in range(n):
    for j in range(i + 1, n):
        A[i][i] = 0
for i in range(n):
    for j in range(0, i):
        A[i][i] = 2

print(A)
