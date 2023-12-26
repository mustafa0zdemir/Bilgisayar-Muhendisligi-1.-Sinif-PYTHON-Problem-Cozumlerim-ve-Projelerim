#Elemanları sıralayan program?
x = [3, 2, 5, 1, 4]

for j in range(4):
    for i in range(4):
        if x[i] > x[i+1]: # yer değiş
            a = x[i]
            x[i] = x[i+1]
            x[i+1] = a
print(x)