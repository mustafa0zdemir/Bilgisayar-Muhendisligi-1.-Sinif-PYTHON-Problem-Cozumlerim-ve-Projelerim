#Matrisin Belirli Bir Satırını Silme: Verilen bir matrisin belirli bir satırını silen bir Python programı yazın.

sil = int(input("silinecek satırı giriniz: "))

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

for i in range(len(m1)):
    for j in range(len(m1[i])):
        if i != sil-1:
            print(m1[i][j], end=" ")
    print()