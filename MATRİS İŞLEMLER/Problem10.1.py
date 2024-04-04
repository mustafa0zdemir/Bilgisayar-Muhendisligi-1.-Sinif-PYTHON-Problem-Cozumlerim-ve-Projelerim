#Matrisin Belirli Bir Elemanını Bulma: Verilen bir matrisin belirli bir elemanını bulan bir Python programı yazın.

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]
n = int(input("aramak istediğiniz elemanı giriniz: "))
c = 1
for i in range(len(m1)):
    for j in range(len(m1[i])):
        if m1[i][j] == n:
            c = 0
if c == 0:
    print(f"{i}.satırın {j}.sutünunda {n} sayısı bulunur")
else:
    print("aradığınız eleman matriste yok")


