#çift sayıları sayının bir üst değeriyle değiştirerek tek sayı yapan algoritma
def TekSayiDonustur(sayilar):
    degisen_sayilar = 0

    for i in range(len(sayilar)-1):
        if sayilar[i] % 2 == 0:
            sayilar[i] += 1
            degisen_sayilar += 1

    if degisen_sayilar > 0:
        print("Yeni liste:", sayilar)
        print(f"Toplamda {degisen_sayilar} adet sayı değiştirildi.")
    else:
        print("Çift sayı bulunamadı.")



TekSayiDonustur([1,2,3,4,5]) //Test değeri
