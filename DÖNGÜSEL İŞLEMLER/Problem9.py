#Girilen bir sayının asal olup olmadığını bulunuz?

sayi = int(input("bir sayı giriniz: "))
if sayi < 2:
    print(f"{sayi} sayısı sayı asal sayı değildir")
elif sayi ==2:
    print(f"{sayi} sayısı asal sayıdır")
else:
    for i in range(2,sayi):
        if sayi % i == 0:
            kontrol = 0
            break
        else:
            kontrol = 1
    if kontrol == 0:
        print(f"{sayi} sayısı sayı asal sayı değildir")
    else:
        print(f"{sayi} sayısı asal sayıdır")