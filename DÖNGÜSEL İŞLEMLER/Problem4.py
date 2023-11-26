#Girilen sayının tam bölenlerini bulan program?

sayi = int(input("sayıyı giriniz "))
liste = []
for i in range(1,sayi+1):
    if sayi % i == 0:
        liste.append(i)
print(f"{sayi} sayısının tam bölenleri {liste}")



