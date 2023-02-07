n = input("Введите свой возраст:")

if int(n) < 1:
    print("Возраст введен неверно")
elif int(n) > 99:
    print("Возраст введен неверно")
elif int(n) == 11:
    print("Мне", n, "лет")
elif int(n[-1]) == 1:
    print("Мне", n, "год")
elif int(n[-1]) == 2:
    print("Мне", n, "года")
elif int(n[-1]) == 3:
    print("Мне", n, "года")
elif int(n[-1]) == 4:
    print("Мне", n, "года")
else:
    print("Мне", n, "лет")