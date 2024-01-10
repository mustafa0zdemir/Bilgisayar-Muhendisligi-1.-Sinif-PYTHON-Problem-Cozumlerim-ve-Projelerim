# Kullanıcıdan boy (cm) ve kilo (kg) bilgilerini aldıktan sonra Vücut Kilo İndeksini (VKİ) hesaplayan ve aşağıdaki tabloya göre Durum bilgisini çıktı veren programı yazınız?

boy = int(input("boyunuzu giriniz (cm) "))
kilo = int(input("kilonuzu giriniz (kg) "))

vki = (100 * kilo)/(boy/10) **2

if vki < 18:
    print(vki,"zayıf")
elif vki < 25:
    print(vki, "normal")
elif vki < 30:
    print(vki,"fazla")
else:
    print(vki,"obez")
