
def SpiralMatrix(m):
    liste = []
    l = 0
    t = 0
    r = len(m[0]) - 1  
    b = len(m) - 1 

    while l <= r and t <= b: 
        for i in range(l, r + 1):
            liste.append(m[t][i])
        t += 1
        for i in range(t, b + 1):
            liste.append(m[i][r])
        r -= 1
        if t <= b:  
            for i in range(r, l - 1, -1):
                liste.append(m[b][i])
            b -= 1
        if l <= r:  
            for i in range(b, t - 1, -1):
                liste.append(m[i][l])
            l += 1
    return (liste)



m = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12]]
print(SpiralMatrix(m))

# leetcode: https://leetcode.com/problems/spiral-matrix/