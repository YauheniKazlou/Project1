slovar1 = {
    "hello": "привет",
    "book": "книга",
    "world": "мир",
}
slovo = input("Введите слово: ")
for key, val in slovar1.items():
    if slovo in slovar1:
        if slovo == key:
            print(val)
        elif slovo == val:
            print(key)
    else:
        print("Введенное слово отсутствует в словаре!")