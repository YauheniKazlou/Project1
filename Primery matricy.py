print("Первый способ создания матрицы:")
n = int(input("Введите колличество строк: "))
m = int(input("Введите колличество столбцов: "))
spis = [0] * n
for i in range(n):
    spis[i] = [0] * m
print(spis)

print("\n"+"Второй способ создания матрицы:")
spis1 = []
for i in range(n):
    spis1.append([0] * m)
print(spis1)

print("\n"+"Третий способ создания матрицы:")

spis2 = [[0] * m for i in range(n)]
print(spis2)
