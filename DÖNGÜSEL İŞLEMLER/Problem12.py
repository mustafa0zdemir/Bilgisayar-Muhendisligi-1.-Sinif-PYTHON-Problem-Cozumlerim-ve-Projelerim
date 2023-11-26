# Girilen iki sayının OKEK (ortak katların en küçüğü) hesaplayan program?
# Girilen iki sayının OBEB (ortak bölenlerin en büyüğü) hesaplayan program?

num1 = int(input("birinci sayıyı giriniz: "))
num2 = int(input("ikinci sayıyı giriniz: "))

if (num1 < num2):
    kucuk = num1
else:
    kucuk = num2
for i in range(1,kucuk+1):
    if num1 % i == 0 and num2 % i == 0:
        ebob = i
        ekok = (num2*num1) // ebob

print(f"iki sayının ebobu {ebob}")
print(f"iki sayının ekoku {ekok}")