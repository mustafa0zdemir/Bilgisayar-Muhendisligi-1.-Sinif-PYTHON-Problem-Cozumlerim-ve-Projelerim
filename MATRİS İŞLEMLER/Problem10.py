#Matrisin Belirli Bir Elemanını Bulma: Verilen bir matrisin belirli bir elemanını bulan bir Python programı yazın.

sayi = int(input("hangi sayıyı araştırmak istiyorsunuz: "))

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

for i in range(len(m1)):
    for j in range(len(m1[i])):
        if m1[i][j] == sayi:
            print(f"{i+1}. satır {j+1}. sütunda {sayi} sayısı yer almaktadır")
        else:
            pass