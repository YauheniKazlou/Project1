import random
n = str(random.randint(1000000000, 9999999999))
print("Случайное десятизначное число -", n)
s = 0
for i in n:
    s += int(i)
print("Сумма цифр этого числа равно -", s)
