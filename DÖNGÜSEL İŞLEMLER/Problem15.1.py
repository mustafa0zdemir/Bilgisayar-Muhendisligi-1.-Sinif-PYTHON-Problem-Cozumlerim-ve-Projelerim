#Girilen sayının basamak değerlerinde k rakamı olmayanları listeleyen program?

sayi = int(input("sayıyı giriniz: "))
k = int(input("istenmeyeni giriniz: "))

k_olmayan_liste = []

while sayi >0:
    son = sayi%10
    if son != k:
        k_olmayan_liste.append(son)
    sayi = sayi // 10 

print(f"{k} sayısının girilen sayıdan çıkarılmış halinin listesi {k_olmayan_liste[::-1]}")
