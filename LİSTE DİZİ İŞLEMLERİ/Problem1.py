#Girilen 5 sayının standart sapmasını bulan program?

liste = []

for i in range(5):
    sayi = int(input(str(i+1)+ ". sayiyi gir "))
    liste.append(sayi)


toplam = 0
for i in range(5):
    toplam += liste[i]

ortalama = toplam / 5

stoplam = 0
for i in range(5):
    stoplam  += (liste[i] - ortalama)**2

standartsapma = (stoplam / 5) ** 0.5

print("sıtandart sapma" , standartsapma)

