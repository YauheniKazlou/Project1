import copy

print("\n", "Список:")
spis = [8, 4, 4, 4, "Hello", -9, 4, 5, 4, 4, None]
print(spis)

print("\n", "Расставляем все элементы списка в обратном порядке:")
spis.reverse()
print(spis)

print("\n", "Добавляем указанный элемент в конец списка:")
spis.append("new")
print(spis)

print("\n", "Добавляем указанный элемент в списке под указанным индексом:")
spis.insert(0, "now")
print(spis)

print("\n", "Выводим под каким индексом в списке расположен указанный элемент (None):")
i = spis.index(None)
print(i)

print("\n", "Удаляем элемент под указанным индексом (1):")
spis.pop(1)
print(spis)

print("\n", "Удаляем последний элемент (если не прописан индекс):")
spis.pop()
print(spis)

print("\n", "Удаляем указанный элемент (8) - удаляется первое вхождение при повторении элемента:")
spis.remove(8)
print(spis)

print("\n", "Проверяем, есть ли элемент (нету) в списке и удаляем его:")
a = "Hell"  # такого элемента нету в списке
if a in spis:
    spis.remove(a)
print(spis)

print("\n", "Проводим подсчет колличества указанных элементов (4) в списке:")
n = spis.count(4)
print(n)

print("\n", "Проводим сортировку списка (цифры):")
spis1 = [5, 6, 3, 34, 34, 56, 345, 0, -3, 67, 12, 310, 7]
spis1.sort()
print(spis1)

print("\n", "Проводим сортировку списка (слова), переводя все буквы в маленькие:")
spis2 = ["Jeff", "Tom", "pol", "ron", "Kry"]
spis2.sort(key=str.lower)
print(spis2)

print("\n", "Проводим сортировку списка (слова) при помощи функции, переводя все буквы в маленькие:")
spis3 = sorted(spis2, key=str.lower)
print(spis3)

print("\n", "Выводим мин и макс значения элементов из списка")
print("мин -", min(spis1))
print("макс -", max(spis1))

print("\n", "Выполняем глубокое копирование и добавляем элемент в конец списка:")
spis4 = copy.deepcopy(spis3)
spis4.append("Jack")
print(spis3, "\n", spis4)

print("\n", "Выполним копирование части списка")
spis5 = spis4[0:5:3]
print(spis5)

print("\n", "Выполним соединение списков")
spis6 = spis4 + spis5
print(spis6)

print("\n", "Список списков:")
si = [
    ["a", "b", "c"],
    [1, 2, 3, 4],
    [None]
    ]
print(si[2])
print(si[0][1])

print("\n", "Добавление в конец списка - нового списка списков:")
si.append(["New", "word"])
print(si[-1])  # выводим добавленный список

print("\n", "Добавление в конец добавленного списка - нового элемента:")
si[-1].append("- best")
print(si)

print("\n", "Удаление из указанного списка указанного элемента:")
si[-1].pop(0)
print(si)

print("\n", "Замена второго списка в списке:")
si[1] = [5, 6, 7]
print(si)

print("\n", "Перебор вложенных списков:")
for si[0] in si:
    for a in si[0]:
        print(a, end='|')
