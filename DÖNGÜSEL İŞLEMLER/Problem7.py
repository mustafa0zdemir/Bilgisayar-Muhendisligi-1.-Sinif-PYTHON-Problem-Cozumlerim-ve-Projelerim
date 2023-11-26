#Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program?

ilk_eleman = int(input("serinin ilk elemanı: "))
toplam_eleman = int(input("toplam eleman sayısı: "))
artıs_degeri = int(input("artış değeri: "))

toplam= 0
index = 1
for i in range(ilk_eleman, toplam_eleman * artıs_degeri + ilk_eleman, artıs_degeri):
    print(index, i)
    index +=1
    toplam += i    
print(f"serinin toplamı {toplam}")

