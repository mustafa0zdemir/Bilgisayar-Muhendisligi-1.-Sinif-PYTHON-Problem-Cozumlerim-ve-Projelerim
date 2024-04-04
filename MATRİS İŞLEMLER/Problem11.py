# Matrisin Sıfıra Eşit Olup Olmadığını Kontrol Etme:*

m1 = [[0,0,0],     # m1 test edilecek matris
      [0,0,0],
      [0,0,0]]         

m2 = [[0 for x in range(len(m1))]for x in range(len(m1[0]))]        #m2 kontrol matrisi


if m1 == m2:
    print("m1 matrisi sıfıra eşit")
else:
    print("m1 matrisi sıfıra eşit değil")