# 1-10 arassı rastgele matris oluşturma sorusu 

import random                                                      
def RastgeleMatrisBas(satir,sutun):
    m = [[0 for x in range(sutun)] for x in range(satir)]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = random.randint(1,10)

    return print(m)

print(RastgeleMatrisBas(5,4))

# fonksiyona verilecek 1. girdi satır sayısını 2. girdi sütun sayısını
# belirlemek için kullanılır
