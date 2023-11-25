#Girilen tamsayının sıfır, pozitif ya da negatif olup olmadığını bulan program?

sayi = int(input("sayıyı giriniz "))
if sayi > 0:
    print(sayi,"sayısı pozitiftir")
elif sayi < 0:
    print(sayi,"sayısı negatiftir")
else:
    print(sayi,"sıfırdır" )

