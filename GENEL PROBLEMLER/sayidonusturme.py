#çift sayıları tek sayı yapan algoritma
def TekSayiDonustur(N, sayilar):
    degisen_sayilar = 0

    for i in range(N):
        if sayilar[i] % 2 == 0:
            sayilar[i] += 1
            degisen_sayilar += 1

    if degisen_sayilar > 0:
        print("Yeni liste:", sayilar)
        print(f"Toplamda {degisen_sayilar} adet yer değiştirme yapıldı.")
    else:
        print("Çift sayı bulunamadı.")



TekSayiDonustur(10,[1,2,3,4,5,6,7,8,9,10])