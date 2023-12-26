#DENGE - 1
'''
A, B ve C ağırlıklarını kullanıcı belirliyor.
Buna göre x’in alabileceği değer aralığını ekrana yazınız?
'''

a = float(input("A AĞIRLIĞINI GİRİNİZ: "))
b = float(input("B AĞIRLIĞINI GİRİNİZ: "))
c = float(input("C AĞIRLIĞINI GİRİNİZ: "))


sagKefe = b + c
solKefe = a 

if sagKefe != solKefe:
    x = (sagKefe - solKefe) / 3
    solKefe += 3 * x

print(int(x-1), "< X <", int(x+1),"X'in değer aralığı ")