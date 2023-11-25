#Çizginin başlangıç ve orta nokta koordinatları veriliyor. Diğer uç noktanın koordinatlarını bulunuz?

x1 = int(input("başlangıç noktasının x değerini giriniz "))
y1 = int(input("başlangıç noktasının y değerinin girniz "))

x2 = int(input("orta noktanın x değerini giriniz "))
y2 = int(input("orta noktanın y değerinin girniz "))

y3 = 2 * y2 - y1
x3 = 2 * x2 - x1
print("uç noktanın koordinatları ", x3,y3 )
