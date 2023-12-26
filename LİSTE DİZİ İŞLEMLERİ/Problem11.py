#Girilen yazıdaki aranan kelimenin önüne ve arkasına TIRNAK sembolünü ekleyen program?
metin = input("metnini gir:  ")
metin += " "      #cümleninin son kelimesini. de döngüde alabilmek
arananKelime= input("hangi kelime:  ")

liste1 = []
kelimeler = ""
sonCumle = ""


for harf in metin:
    if " " != harf:
        kelimeler += harf
    else:
        liste1.append(kelimeler)
        kelimeler = ""

for kelime in liste1:
    if kelime == arananKelime:
       kelime = "\"" + kelime + "\""
    sonCumle += kelime + " "
print(sonCumle)
