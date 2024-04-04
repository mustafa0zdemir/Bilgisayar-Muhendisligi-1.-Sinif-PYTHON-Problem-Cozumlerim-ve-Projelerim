#bir matrisi bir sayı ile çarpma

sayi = int(input("matrisi çarpmak istediğiniz sayıyı giriniz: "))

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

m2 = [[0,0,0],
      [0,0,0],
      [0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[i])):
        m2[i][j] = m1[i][j] * sayi

for liste in m2:
    print(liste)