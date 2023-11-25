#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))

if sayi1 > sayi2 and sayi1 > sayi3:
    print("En büyük sayı: ",sayi1)
elif sayi2 > sayi1 and sayi2 > sayi3:
    print("En büyük sayı: ",sayi2)
else:
    print("En büyük sayı: ",sayi3)





