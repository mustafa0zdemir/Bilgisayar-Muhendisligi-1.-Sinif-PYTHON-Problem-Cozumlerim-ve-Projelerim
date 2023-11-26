# TC kimlik noyu doğru girmeye zorlayınız? (11 karakter ve tamamı sayı)
while True:
    tc_kimlik = input("Lütfen 11 haneli TC kimlik numaranızı girin: ")
    
    if len(tc_kimlik) != 11 or not tc_kimlik.isdigit():
        print("Giriş başarısız. TC kimlik numaranızı tekrar girerek giriş yapmayı deneyiniz")
    else:
        print("Giriş başarılı. Teşekkür ederiz!")
        break
