# Listede tekrarlanan sayıları bulan program ?
x = [3, 1, 2, 3, 5, 3, 6, 7, 0, 2, 4, 7, 8, 9, 4]
tekrarListesi = []
for i in x:
    kontrol = 0
    for k in tekrarListesi:
        if k == i:
            kontrol = 1
            break

    if kontrol == 0:
        tekrarListesi.append(i)

        tekrar = 0
        for j in x:
            if i == j:
                tekrar += 1

        print(str(i)+" sayısı "+str(tekrar)+" defa tekrar ediyor")