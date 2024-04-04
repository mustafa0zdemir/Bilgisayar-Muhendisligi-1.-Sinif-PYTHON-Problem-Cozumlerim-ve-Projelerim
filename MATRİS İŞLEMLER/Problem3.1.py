#Matris izini (diyagonal toplam) bul.
m1 = [[1,2,3],
     [4,5,6],
     [7,8,9]]
diyogonal = 0
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if i == j:
            diyogonal += m1[i][j]
print(diyogonal)