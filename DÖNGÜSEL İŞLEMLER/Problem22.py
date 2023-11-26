




sayi = int(input("lütfen tablo ölçüsünü giriniz: "))
print(" ",end=" ")
for sutun in range(1, sayi+1):
    print("{0:4}".format(sutun), end=" ")
print()
print("+", end=" ")
for sutun in range(1, sayi+1):
    print("-----", end="")
print()
for satir in range(1, sayi+1):
    print("{0:3}|".format(satir),end=" ")
    for sutun in range(1, sayi+1):
        deger = satir*sutun
        print("{0:4}".format(deger),end=" ")
    print()