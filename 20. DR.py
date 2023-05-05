print("Первая задача:")

strs = "слово не слово или не слово"
strs = strs.split()
print(strs)

strs1 = []
for i in strs:
    if i not in strs1:
        strs1.append(i)
        print("Кол-во вхождений в строку слова", "\""+i+"\" -", strs.count(i))

print("\nВторая задача:")

str1 = "3"
str2 = "слова только слова"
str3 = "цифры только цифры"
str4 = "слова и цифры"

text = list(str1.split()) + list(str2.split()) + list(str3.split()) + list(str4.split())  # весь текст представленный в виде одного списка
list1 = []  # список слов, которые есть в тексте
dict1 = {}

for i in text:
    if i not in list1:
        list1.append(i)
        print("Кол-во вхождений в текст слова", "\"" + i + "\" -", text.count(i))
for i in list1:
    dict1[i] = text.count(i)
print("Получился словарь с количеством упоминаний в первоначальном тексте каждого слова -", dict1)
val1 = []  # список цифр, которые указывают на количество упоминаний каждого слова в тексте
for j in dict1.values():
    val1.append(j)
list2 = []  # слово или несколько слов, которые макс кол-во раз встречаются в тексте
for key, val in dict1.items():
    if max(val1) == val:
        list2.append(key)
if list2[0] < list2[1]:
    print("Слово", "\""+list2[0]+"\"", "меньше в лексиокографическом порядке.")
else:
    print("Слово", "\""+list2[1]+"\"", "меньше в лексиокографическом порядке.")
