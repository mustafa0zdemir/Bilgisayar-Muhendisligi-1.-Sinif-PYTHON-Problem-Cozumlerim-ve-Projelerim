#Girilen onluk sayıyı ikili sayıya dönüştürünüz?

x = int(input("sayı gir: "))
ikiliksayı = ""
while x > 0:
    ikiliksayı =str(x%2) + ikiliksayı
    x = x//2
print(ikiliksayı)
