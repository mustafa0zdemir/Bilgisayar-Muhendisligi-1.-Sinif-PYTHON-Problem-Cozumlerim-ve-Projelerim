#Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program?

n = int(input(" n değerini giriniz: "))
k = int(input(" k değerini giriniz: "))

sum = 0

for i in range(1,n+1,1):
    sum += i * k
print(sum)
 