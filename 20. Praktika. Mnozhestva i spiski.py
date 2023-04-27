n = int(input("Введите кол-во элементов списка: "))
spis1 = []
for i in range(n):
    spis1.append(input("-новый элемент: "))
print(spis1)
spis2 = []
for i in spis1:
    if i not in spis2:
        spis2.append(i)
spis2.sort()
print(spis2)
