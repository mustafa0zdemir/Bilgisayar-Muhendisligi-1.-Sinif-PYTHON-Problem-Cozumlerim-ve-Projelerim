#Vize ve Final notu girilen öğrencinin geçip geçmediğini hesaplayan program (vizenin %40,finalin %60’ı hesaplanır. Final en az 60 olmak zorundadır)

vize = int(input("vize notunu giriniz "))
final = int(input("final notunu girin "))
ortalama = vize*0.4 + final*0.6
if final < 60:
    print("öğrenci kaldı")
elif ortalama >= 45:
    print("öğrenci geçti")
else:
    print("öğrenci kaldı")

