#Matrisin Belirli Bir Satırındaki Elemanları Bölme: Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla bölen bir Python programı yazın.

böl = int(input("bölen değerini giriniz"))
satir = int(input("bölünecek satırı giriniz"))

m = [[1,2,3],
      [4,5,6],
      [7,8,9]]

for i in range(len(m)):
    for j in range(len(m[i])):
        m[satir-1][j] = m[satir-1][j]/böl

print(m)
