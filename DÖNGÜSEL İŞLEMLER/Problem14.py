# Girilen sayının basamak değerleri çarpımını bulunuz?

num = int(input("sayıyı giriniz: "))
sayı = num
liste = []
index = 1
listeindex = 0
basamakDeğerlerininÇaprpımı = 1
while num > 0:
    sonrakam = num % 10
    sonrakam*=index
    liste.append(sonrakam)
    index *= 10 
    basamakDeğerlerininÇaprpımı *= liste[listeindex]
    listeindex += 1
    num = num //10 
print(f"{sayı} sayısının basamak değerlerinin yazılı olduğu liste {liste}")
print(f"{sayı} sayısının basamak değerlerinin çarpımı {basamakDeğerlerininÇaprpımı}")
