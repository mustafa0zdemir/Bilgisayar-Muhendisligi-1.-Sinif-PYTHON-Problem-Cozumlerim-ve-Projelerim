#Farklı değerlere sahip iki listenin korelasyon katsayısını hesaplayan program?

x = [1,2,3,4,5,6,7]
y = [9,8,10,12,11,13,14]

toplamA = 0
for i in range(7):
    carpım = x[i] * y[i]
    toplamA += carpım
ortalamaA = toplamA /7

toplamY = 0
toplamX = 0
for i in range(7):
    toplamX += x[i]
    toplamY += y[i] 

ortX = toplamX /7
ortY = toplamY /7

pay = ortalamaA - (ortX * ortY)

xkaretoplam = 0
ykaretoplam = 0
for i in range(7):
    xkaretoplam += x[i]**2
    ykaretoplam += y[i]**2

ykareort = ykaretoplam / 7
xkareort = xkaretoplam / 7

payda = ((xkareort - (ortX**2))**0.5) * ((ykareort - (ortY**2))**0.5)

korelasyonKatsayısı = pay / payda
print(korelasyonKatsayısı)