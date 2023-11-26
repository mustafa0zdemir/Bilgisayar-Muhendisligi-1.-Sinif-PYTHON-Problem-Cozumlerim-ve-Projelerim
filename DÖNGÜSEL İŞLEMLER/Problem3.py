#N’e kadar tek sayıları yazdıran program?

liste = []
sayi = int(input("N= "))
for i in range(sayi):
    if i % 2 == 1:
        liste.append(i)

print(f"N e kadar olan tek sayıların listesi {liste}")
