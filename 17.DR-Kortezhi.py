st = 1, 3, 7, 9, 1, 3, 7, "Tom", 45, "Yan", "Tom", 1, 1
print("Исходная строка -", st)
str_spis = []
for i in st:
    str_spis.append(i)
print("Исходный список -", str_spis)
str_new = []
for item in str_spis:
    if item not in str_new:
        str_new.append(item)
print("Отредактированный список -", str_new)
tuple1 = tuple(str_new)
print("Кортеж -", tuple1)
