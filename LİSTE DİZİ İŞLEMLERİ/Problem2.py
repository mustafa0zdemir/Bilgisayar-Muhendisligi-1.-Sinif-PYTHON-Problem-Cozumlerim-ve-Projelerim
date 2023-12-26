# Girilen sayının listede olup olmadığını bulan program?

liste = [1,2,3,4,5,6,7,8]

sayi = int(input("sayıyı gir "))
for i in range(len(liste)):
    if sayi == liste[i]:
        kontrol = 1
        break
    else:
        kontrol = 0

if kontrol == 1:
    print("girilen sayı listede")
else:
    print("girilen sayı listede değil")
    
