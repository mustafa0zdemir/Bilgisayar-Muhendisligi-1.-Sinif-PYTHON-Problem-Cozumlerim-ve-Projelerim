liste = [2,1,5,6,3,4]


for i in range(1,len(liste)):
    key = liste[i]
    j = i -1
    while j >=0 and key < liste[j]:
        liste[j+1] =liste[j]
        j -= 1
    liste[j+1] = key
print(liste) 