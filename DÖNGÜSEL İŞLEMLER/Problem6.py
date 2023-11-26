#Girilen n adet sayı içerisinden pozitif, negatif ve sıfır sayısının kaçar adet tekrarlandığını bulan program?

pozitif = []
negatif = []
sıfır = []


while 1:
    n = input("sayı dizinini giriniz sistemden çıkış yapmak için 'q/Q' tuşuna basınız...  " )
    if n == 'q' or n == 'Q':
        break
    if int(n) > 0:
        pozitif.append(n)
    elif int(n) < 0:
        negatif.append(n)
    else:
        sıfır.append(n)


print(f"pozitif sayıların listesi {pozitif} ve sayısı {len(pozitif)}")
print(f"negatif sayıların listesi {negatif} ve sayısı {len(negatif)}")
print(f"sıfırların listesi {sıfır} ve sayısı {len(sıfır)}")       







