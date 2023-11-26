# 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python Örneği
##kullanıcının istediği sayılara tam bölünen ve istediği araklıktaki değerleri yazdırmasını sağlayan senaryonun çözümü

a = int(input("aralığın başlangıç değerini giriniz "))
b = int(input("aralığın bitiş değerini giriniz "))

x = int(input("1. böleni giriniz "))
y = int(input("2. böleni giriniz "))
for i in range(a,b+1):
    if (i%x == 0) and (i%y == 0):
        print(i)

