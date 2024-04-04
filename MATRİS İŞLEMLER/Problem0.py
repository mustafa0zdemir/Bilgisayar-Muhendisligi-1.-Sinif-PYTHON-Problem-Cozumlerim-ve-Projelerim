# Matrisin satır ve sütun toplamlarını hesapla.

m = [[1,2,3],
    [4,5,6],
    [7,8,9]]

top = 0
for i in range(len(m)):
    for k in range(len(m[i])):
        top += m[i][k]

print(top*2)