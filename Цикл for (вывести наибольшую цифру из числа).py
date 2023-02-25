try:
    chis = input("Введите пятизначное натуральное число: ")
    if len(chis) != 5:
        print("Число должно быть пятизначным!")
    if int(chis[0]) >= (int(chis[1]) or int(chis[2]) or int(chis[3]) or int(chis[4])):
        print("Наибольшая цифра числа " + "\"" + str(chis) + "\"" + " - " + str(chis[0]))
    elif int(chis[1]) >= (int(chis[2]) or int(chis[3]) or int(chis[4])):
        print("Наибольшая цифра числа " + "\"" + str(chis) + "\"" + " - " + str(chis[1]))
    elif int(chis[2]) >= (int(chis[3]) or int(chis[4])):
        print("Наибольшая цифра числа " + "\"" + str(chis) + "\"" + " - " + str(chis[2]))
    elif int(chis[3]) >= int(chis[4]):
        print("Наибольшая цифра числа " + "\"" + str(chis) + "\"" + " - " + str(chis[3]))
    else:
        print("Наибольшая цифра числа " + "\"" + str(chis) + "\"" + " - " + str(chis[4]))

except ValueError:
    print("Вводите только числа!")
