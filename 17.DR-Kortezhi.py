a = 'hello world'
print(a)
a1 = a.split()
print(a1)
r = []
for i in a1:
    r.append(i[0])
print(tuple(r))
