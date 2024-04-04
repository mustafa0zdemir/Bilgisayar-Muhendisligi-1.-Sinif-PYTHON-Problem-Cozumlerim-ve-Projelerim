# Matrisin transpozunu alın.

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

mt = [[0,0,0],
      [0,0,0],
      [0,0,0]]

for i in range(len(m)):
    for j in range(len(m[i])):
        mt[j][i] = m[i][j]

print(mt)


#bu çıktı transpoz işleminin daha net anlaşılabilmesi için oluşturulmuştur
for matris in  mt:
    print(matris)