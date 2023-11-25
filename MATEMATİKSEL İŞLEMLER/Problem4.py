
#  100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme çeviriniz?

ogrencinin_notu = int(input('NOTUNUZU GİRİNİZ : '))
if ogrencinin_notu > 0 and ogrencinin_notu < 45:
    print(f"{ogrencinin_notu} NOTUNUN 5 LİK SİSTEMDE KARŞILIĞI: 1 ")
elif ogrencinin_notu > 44 and ogrencinin_notu < 55:
    print("NOTUNUN 5 LİK SİSTEMDE KARŞILIĞI: 2 ")
elif ogrencinin_notu > 54 and ogrencinin_notu < 70:
    print("NOTUNUN 5 LİK SİSTEMDE KARŞILIIĞI: 3 ")
elif ogrencinin_notu > 69 and ogrencinin_notu < 85:
    print("NOTUNUN 5 LİK SİSTEMDE KARŞILIĞI: 4 ")
elif ogrencinin_notu > 84 and ogrencinin_notu < 101:
    print("NOTUNUN 5 LİK SİSTEMDE KARŞILIĞI: 5 ")
else:
    print("HATALI GİRİŞ YAPTINIZ...")

