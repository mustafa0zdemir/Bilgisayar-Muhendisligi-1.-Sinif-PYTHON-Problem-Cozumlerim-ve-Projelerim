#Matristeki en büyük sayıyı bul.

m1 = [[1,2,3],
     [4,5,6],
     [7,8,9]]

mak = 0
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if mak < m1[i][j]:
            mak = m1[i][j]
        else:
            pass

print(mak)