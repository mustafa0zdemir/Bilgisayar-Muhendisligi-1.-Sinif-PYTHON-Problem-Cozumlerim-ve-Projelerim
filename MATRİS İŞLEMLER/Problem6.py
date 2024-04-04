# GİRİLEN N DEĞERİNE GÖRE 0-100 ARASI NxN BOYUTLU RASTGELE SAYILARLA MATRİS OLUŞTURAN ALGORİTMA

import random
n = int(input("n = "))

m = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        t = round(random.random()*100)
        m[i][j] = t
        
for k in range(len(m)):
    for l in range(len(m[k])):
        print(m[k][l], end=" ")
    print()
print()


# farklı yazım şekillerinde çıktı almak için bu kısım kullanılabilir
# 1. seçenek
for matris in m:          
    print(matris)

print()

# 2. seçenek
print(m)