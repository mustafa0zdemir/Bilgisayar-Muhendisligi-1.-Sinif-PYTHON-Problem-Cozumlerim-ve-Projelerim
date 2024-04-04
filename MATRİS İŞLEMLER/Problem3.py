#Matris izini (diyagonal toplam) bul.

m1 = [[1,2,3],
     [4,5,6],
     [7,8,9]]

diyagonal = 0

i = 0
k = 0
while i < len(m1):
    diyagonal += m1[i][k]
    i +=1
    k +=1
print(diyagonal)