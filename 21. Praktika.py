a = "21. Praktika.txt"
with open(a, "r") as file:
    spis1 = file.readlines()
    for i in spis1:
        print("Элементы", spis1.index(i) + 1, "строки текста:", i, end="")
        print("Кол-во элементов", spis1.index(i) + 1, "строки текста:", len(i.replace("\n", "")), "\n")
