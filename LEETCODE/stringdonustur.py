
# bir sayıda bulunan rakamların adedini yazdıran program
def Strdonus(sayi):
    sayiAdet = 1
    donusum = ''
    for i in range(len(sayi)):
        if i+1 < len(sayi) and sayi[i] == sayi[i+1]:
            sayiAdet += 1
        else:
            donusum += str(sayiAdet) + sayi[i]
            sayiAdet = 1
    return donusum

print(Strdonus("3322251"))
