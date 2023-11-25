# Fiyat ve kdv oranı girilen ürünün toplam fiyatını ekrana yazdıran program?

f =float(input("ürünün kdv siz fiyatını giriniz: "))
k = float(input("kdv oranını giriniz(%): "))

toplam_fiyatı = (f*k/100) + f

print("toplam fiyat",toplam_fiyatı)
