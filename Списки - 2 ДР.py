a = int(input("Введите число начала списка: "))
b = int(input("Введите число окончания списка: "))
spis = list(range(a, b + 1))
print("Список -", spis)
summ = 0
for j in spis:
    summ += j
sred_orif = summ / len(spis)
print("Средне-орифметическое всех элементов списка:", sred_orif)
print("Элементы из списка, значение которых меньше ср-ориф всех элементов:")
for i in spis:
    if i < sred_orif:
        print(i, end=' ')
