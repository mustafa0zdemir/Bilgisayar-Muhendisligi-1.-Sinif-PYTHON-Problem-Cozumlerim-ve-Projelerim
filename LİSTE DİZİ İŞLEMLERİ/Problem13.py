#Girilen onluk sayıyı onaltılık sayıya dönüştürünüz?

x = int(input("sayı gir: "))
onaltılık = ""
while x > 0:
    onaltılık=str(x%16) + onaltılık
    x = x//16
print(onaltılık)
