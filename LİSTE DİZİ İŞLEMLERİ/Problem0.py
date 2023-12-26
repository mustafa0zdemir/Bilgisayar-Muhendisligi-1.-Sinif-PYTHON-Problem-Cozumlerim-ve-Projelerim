#Girilen 5 sayının ortalamasını bulan program?
liste = []

for i in range(5):
    sayi = int(input(str(i+1)+ ". sayiyi gir "))
    liste.append(sayi)

print(f"girilen sayıların lsitesi {liste}")

toplam = 0
for i in range(5):
    toplam += liste[i]
print(f"girilen 5 sayının ortalamsı {toplam/5}")