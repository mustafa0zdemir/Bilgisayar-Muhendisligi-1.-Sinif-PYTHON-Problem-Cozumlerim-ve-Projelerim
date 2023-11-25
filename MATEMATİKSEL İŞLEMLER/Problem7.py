#Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program?

sayi = int(input("3 basamaklı sayıyı giriniz: "))

birler = sayi % 10
onlar = (sayi // 10) % 10
yuzler = sayi // 100

print("Yüzler basamağı:", yuzler*100)
print("Onlar basamağı:", onlar*10)
print("Birler basamağı:", birler)
