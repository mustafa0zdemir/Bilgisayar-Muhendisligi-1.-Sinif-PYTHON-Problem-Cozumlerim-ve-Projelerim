# İşçi maaşı ve çocuk sayısı verilmektedir. Çocuk sayısı bir ise %5, iki ise %10, üç veya daha fazla ise %15 zam yaparak yeni maaşı hesaplayınız?

maas = int(input("İŞÇİ MAAŞINI GİRİNİZ: "))
cocuksayısı = int(input("ÇOCUK SAYISINI GİRİNİZ: "))
yenimaas_1 = maas / 100 * 105
yenimaas_2 = maas / 100 * 110
yenimaas_3 = maas / 100 *115

if cocuksayısı == 1:
    print(f"YENİ MAAŞ: {yenimaas_1}")
elif cocuksayısı == 2 :
    print(f"YENİ MAAŞ: {yenimaas_2}")
elif cocuksayısı >= 3 :
    print(f"YENİ MAAŞ: {yenimaas_3}")
else:
    print(maas)
