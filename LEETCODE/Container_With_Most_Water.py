def maxArea(l):
    mak = 0
    jdeger = 0
    ideger = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            kenar1 = j-i
            kenar2 = min(l[i],l[j])
            alan = kenar1*kenar2

            if mak < alan:
                mak = alan
                ideger = i
                jdeger = j
            
    return [mak,ideger,jdeger]

l = [8,8,6,2,5,4,8,3,9]
l2 = [1,8,6,2,5,4,8,3,7]
print(maxArea(l2))
print(maxArea(l))

