print("Задача №1:")
comp1 = {"IT-Company", "ITT", "IT-Projekt", "IT-Overone"}
comp2 = {"IT-Overone", "ITT", "Skillcompany"}
print("Первое множество -", comp1)
print("Второе множество -", comp2)
print("Обшие объекты обоих множеств:", comp1.intersection(comp2))

print("\n""Задача №2:")
import random
n = int(input("Введите количество множеств: "))
set1 = []
for i in range(n):
    set2 = set()
    for j in range(random.randint(1, 5)):
        set2.add(random.randrange(10))
    set1.append(set2)
    print(set2, end=' ')
print("\n""Множества, кратные трем и не входящие в первое множество:")
for i in set1:
    if len(i) == 3:
        if set1[0].issuperset(i):
            continue
        else:
            print(i, end=' ')
