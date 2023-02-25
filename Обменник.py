print("Для выхода нажмите Y")
while True:
    a = input("Введите любое число или букву: ")
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    if money < 0:
        print("Введенная сумма должна быть положительной!")
        continue  # выполняем переход к первой итерации цикла
    cache = money // 2.8
    ost = round(money % 2.8)
    print("К выдаче", cache, "долларов\n - Ваша сдача", ost, "рублей")
print("Работа обменного пункта завершена.")
