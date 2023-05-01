slovar1 = {
    "hello": "привет",
    "book": "книга",
    "world": "мир"
}
slovo = input("Введите слово: ")
for key, val in slovar1.items():
    if slovo == key:
        print(val)
    elif slovo == val:
        print(key)