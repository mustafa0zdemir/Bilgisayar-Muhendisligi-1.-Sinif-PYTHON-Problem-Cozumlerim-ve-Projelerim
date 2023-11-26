# n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program?

n = int(input(" N değerini giriniz: "))
tektoplam = 0
ciftcarpim = 1

for i in range(1,n):
    if i % 2 == 0:
        ciftcarpim *= i
        
    else:
        tektoplam += i 
        

print(f"TEK SAYILARIN TOPLAMI: {tektoplam}")
print(f"ÇİFT SAYILARIN ÇARPIMI: {ciftcarpim}")       

