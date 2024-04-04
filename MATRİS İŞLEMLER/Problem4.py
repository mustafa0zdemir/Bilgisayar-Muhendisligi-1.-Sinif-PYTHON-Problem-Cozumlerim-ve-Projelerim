# Verilen sayıyı matrisin k. indeksine yerleştir?
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

sayi = int(input("sayıyı gir"))
satir = int(input("kaçıncı satıra yerleştirilecek"))
sutun = int(input("kacıncı sutuna yerleştirilecek"))

m[satir - 1][sutun - 1] = sayi
print(m)