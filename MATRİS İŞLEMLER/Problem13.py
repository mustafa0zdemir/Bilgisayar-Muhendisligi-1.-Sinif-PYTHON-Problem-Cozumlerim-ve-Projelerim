#Matrisin Belirli Bir Sütununu Silme: Verilen bir matrisin belirli bir sütununu silen bir Python programı yazın.

sil = int(input("silinecek sütunu giriniz: "))

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

for i in range(len(m1)):
    for j in range(len(m1[i])):
        if j != sil-1:
            print(m1[i][j], end=" ")
    print()
