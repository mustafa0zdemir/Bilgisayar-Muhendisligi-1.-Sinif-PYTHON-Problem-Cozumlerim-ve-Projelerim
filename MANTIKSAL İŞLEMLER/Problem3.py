#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))
en_buyuk = max(sayi1, sayi2, sayi3)
print(f"En büyük sayı: {en_buyuk}")
