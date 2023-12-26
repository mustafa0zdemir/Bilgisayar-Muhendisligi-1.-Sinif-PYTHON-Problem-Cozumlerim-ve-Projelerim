#Her elemanın tekrar sayısını bulan program?
liste = [3, 3, 3, 2, 2, 1, "armut", "elma", "muz", "muz", 1]
tekrarlar = {}

for eleman in liste:
    tekrar_sayisi = liste.count(eleman)
    tekrarlar[eleman] = tekrar_sayisi

print(tekrarlar)
