# f(x) = ax^2 - bx -c fonksiyonunun x eksenini kestiği nokta sayısını bulunuz?

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
delta = b**2 - 4*a*c
if delta<0:
	print("KÖK YOK")
else:
	x1 = (-b - delta ** 0.5) / (2*a)
	if delta == 0:
		print(f"Bir kök var {x1}")
	else:
		x2 = (-b + delta**0.5) / (2*a)
print(f"İki kök var x1 = {x1} , x2 = {x2}")










