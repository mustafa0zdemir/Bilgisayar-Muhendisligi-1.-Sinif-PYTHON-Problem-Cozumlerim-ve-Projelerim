#  Bir ürünün alış fiyatı, vergi ve kar oranlarını kullanılarak satış fiyatını hesaplayan program?

urun_fiyat = float(input("ÜRÜNÜN FİYATINI GİRİNİZ: "))
kdv_oran = float(input("KDV ORANINI GİRİNİZ: %"))
kar = float(input("KAR ORANINI GİRİNİZ: %"))
kdvli_urun = (urun_fiyat * kdv_oran / 100) + urun_fiyat 
satis_fiyatı = (kdvli_urun * kar / 100) + kdvli_urun
print("SATIŞ FİYATI: ", satis_fiyatı)
