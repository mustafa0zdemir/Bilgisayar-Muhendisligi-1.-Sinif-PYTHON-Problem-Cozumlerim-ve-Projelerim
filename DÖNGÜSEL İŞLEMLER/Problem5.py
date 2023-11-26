# Girilen n değerine göre Fibonacci serisinin ( 0 1 1 2 3 5 8 ... ) ilk n terimini hesaplayınız?

n = int(input("n değerini girin: "))

liste = [0, 1]  # İlk iki terim
if n == 1:
    liste = [0]  # İlk terim
elif n > 1:
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        liste.append(b)

print(liste)




