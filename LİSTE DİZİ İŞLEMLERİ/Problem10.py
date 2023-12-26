#Girilen yazının k. karakteriyle r. karakteri arasını kopyalayan programı yazınız?

metin = input("metni giriniz: ")

deger1 = int(input("ilk karakteri giriniz: "))
deger1 -= 1                                         
deger2= int(input("son karakteri giriniz: "))

print(metin[deger1:deger2])