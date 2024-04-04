# Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.

n = int(input(" N değerini giriniz: "))

m = [[0 for x in range(n)]for x in range(n)]

dx = 1
for i in range(n):
    for j in range(n):
        m[i][j] = dx
        dx += 1

for matris in m:
    print(matris)



