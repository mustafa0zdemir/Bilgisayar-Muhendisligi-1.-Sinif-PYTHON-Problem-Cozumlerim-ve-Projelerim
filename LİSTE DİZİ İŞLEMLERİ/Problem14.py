#Girilen ikilik sayıyı onluk sayıya dönüştürünüz?

x = int(input("ikilik sayıyı giriniz: "))

onluk = 0
i = 0
while x > 0:
    sonbasamak = (x % 10) * 2**i
    onluk += sonbasamak
    x = x // 10
    i += 1
print(onluk)

