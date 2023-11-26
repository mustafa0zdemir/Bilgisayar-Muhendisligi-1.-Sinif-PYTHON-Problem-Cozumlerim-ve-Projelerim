








num = int(input("lütfen tablo ölçüsünü giriniz: "))
for satir in range(1, num+1):
    for sutun in range(1, num+1):
        deger = satir*sutun
        print("{0:4}".format(deger), end=" ")
    print() 