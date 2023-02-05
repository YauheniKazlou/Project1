name = "Евгений"
user = "Козлов"
age = 26

enter = input("Введите свое имя:")
enter3 = input("Введите свою фамилию:")
enter2 = int(input("Введите свой возраст:"))

text = name == enter and age == enter2 and user == enter3

if text == False:
    print("Доступ запрещен")
    if name != enter:
        print("Неверно введено имя")
    if user != enter3:
        print("Неверно введена фамилия")
    if age != enter2:
        print("Неверно введен возраст")
else:
        print("Доступ разрешен")

