# Задача №1:
klass = "11B_klass.txt"
ocenki = {
    "Иванов Иван - ": "4\n",
    "Петров Петр - ": "2\n",
    "Сидоров Егор - ": "7\n",
    "Емельянов Артем - ": "3\n",
    "Акулич Александр - ": "1\n"
}
with open(klass, "w") as file:
    for i, j in ocenki.items():
        file.write(i)
        file.write(j)
with open(klass, "r") as file:
    for i in file:
        print(i, end="")
with open(klass, "a") as file:
    file.write("\nУчащиеся 11Б класса, имеющие оценку ниже 3:\n")
    print("\nУчащиеся 11Б класса, имеющие оценку ниже 3:")
    for i, j in ocenki.items():
        if int(j) < 3:
            file.write(i)
            file.write(j)
            print(i, j, end="")
    summ = 0
    for i in ocenki.values():
        summ += int(i)
        sr = summ/len(ocenki)
    file.write("\nСредний балл класса: ")
    file.write(str(sr))
    print("\nСредний балл класса:", sr)

print("\nЗадача №2:")
new_file = "new_text.txt"
a = int(input("Введите кол-во строк текста: "))
text = []
for i in range(a):
    str_new = input("Введите данные " + str(i+1) + "-й строки: ")
    text.append(str_new)

with open(new_file, "w") as file:
    for i in text:
        file.write(i)
        file.write("\n")

with open(new_file, "r") as file:
    for i in file:
        print(i, end="")

print("\nЗадача №2.2:")

with open("1.txt", "w") as fl:
    while True:
        a = input("Введите данные строки: ")
        if a == "":
            break
        fl.write(a + "\n")


