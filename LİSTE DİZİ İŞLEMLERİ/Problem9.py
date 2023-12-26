#Girilen yazının büyük yazılıp yazılmadığını bulan program?

büyükHarfler = ["Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","K","J","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç"]
metin = input("metni giriniz: ")

for i in range(len(metin)):
    if metin[i] in büyükHarfler:
        kontrol = 1
        break
    else:
        kontrol = 0

if kontrol == 1:
    print(metin,"GİRİLEN YAZI BÜYÜK KARAKTERLER İÇERİYOR")
else: 
    print(metin,"GİRİLEN YAZI BÜYÜK KARAKTERLER İÇERMİYOR") 
