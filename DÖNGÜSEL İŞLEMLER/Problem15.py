#Girilen sayının basamak değerlerinde k rakamı olmayanları listeleyen program?

sayi = int(input("sayıyı giriniz"))
k = int(input("istenmeyeni giriniz: "))

while sayi >0:
    son = sayi%10
    if son != k:
        print(son)
    sayi = sayi // 10 