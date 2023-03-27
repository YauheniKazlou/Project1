s1 = [1, 2, 3, 4]
s2 = [5, 6, 7, 8]
S = [s1, s2]
print(S)
summ = 0
for i in range(len(S)):
    for j in range(len(S[i])):
        print(S[i][j], end=' ')
        summ += S[i][j]
print("\n", summ)
