#Girilen sayının 6'nın katı olduğunu bulan program?

num = int(input("SAYIYI GİRİNİZ: "))

process = num % 6
if process == 0:
    print(f"{num} SAYISI 6 NIN TAM KATIDIR")
else:
    print(f"{num} SAYISI 6 NIN TAM KATI DEĞİLDİR")

