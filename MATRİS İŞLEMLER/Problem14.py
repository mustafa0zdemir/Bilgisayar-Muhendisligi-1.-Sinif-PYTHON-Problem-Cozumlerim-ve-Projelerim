#Matris Elemanlarının Mutlak Değerini Alma: Verilen bir matrisin elemanlarının mutlak değerini alan bir Python programı yazın.

m = [[1,-2,3],
      [4,5,-6],
      [7,-8,9]]

for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = abs(m[i][j])

print(m)

