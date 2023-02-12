str1 = str(input("Введите слово: "))
if str1 == str1[-1::-1]:
    print("Слово \"" + str.capitalize(str1) + "\"" + " - палиндром")
else:
    print("Слово \"" + str.capitalize(str1) + "\"" + " - не является палиндромом")
