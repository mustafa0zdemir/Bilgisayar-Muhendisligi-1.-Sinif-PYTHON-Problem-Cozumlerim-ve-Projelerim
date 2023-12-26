# Girilen yazıdaki boşluk karakter sayısını bulan program?

metin =input("metni giriniz: ")
print(f"girilen metin: {metin}")
sayac = 0
for i in metin:                
    if i == " ": 
        sayac += 1           

print(f"boşluk karakter sayısı: {sayac}")

