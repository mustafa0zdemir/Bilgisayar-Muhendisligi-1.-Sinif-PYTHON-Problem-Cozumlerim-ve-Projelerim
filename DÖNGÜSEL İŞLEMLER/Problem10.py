#Girilen sayının basamak sayısını bulunuz?

sayi = int(input("sayıyı giriniz: "))
toplambasamaksayısı = 0
while sayi >0:
    son = sayi%10
    sayi = sayi // 10
    toplambasamaksayısı += 1
print(f"toplam basamak sayısı {toplambasamaksayısı}")
