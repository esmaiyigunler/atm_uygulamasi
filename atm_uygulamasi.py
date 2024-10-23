
kullaniciAdlari = ["Ali", "Ayşe", "Fatih", "Esra"]
kullaniciSifreleri = ["1234", "5678", "4321", "9876"]
kullaniciBakiyeleri = [1000, 2000, 1500, 5000]


def kullaniciIndeksi(kullaniciAdlari, kullaniciAdi):
    if kullaniciAdi in kullaniciAdlari:
        return kullaniciAdlari.index(kullaniciAdi)
    else:
        return -1


def bakiyeGoruntule(kullaniciBakiyeleri, kullaniciIndeksi):
    print("Mevcut Bakiyeniz:", kullaniciBakiyeleri[kullaniciIndeksi], "TL")


def paraCek(kullaniciBakiyeleri, kullaniciIndeksi, miktar):
    if kullaniciBakiyeleri[kullaniciIndeksi] >= miktar:
        kullaniciBakiyeleri[kullaniciIndeksi] -= miktar
        print(miktar, "TL çektiniz. Güncel bakiyeniz:", kullaniciBakiyeleri[kullaniciIndeksi], "TL")
    else:
        print("Yetersiz Bakiye")


def paraYatir(kullaniciBakiyeleri, kullaniciIndeksi, miktar):
    kullaniciBakiyeleri[kullaniciIndeksi] += miktar
    print(miktar, "TL yatırdınız. Güncel bakiyeniz:", kullaniciBakiyeleri[kullaniciIndeksi], "TL")

def sifreDegistir(kullaniciSifreleri, kullaniciIndeksi, eskiSifre, yeniSifre):
    if kullaniciSifreleri[kullaniciIndeksi] == eskiSifre:
        kullaniciSifreleri[kullaniciIndeksi] = yeniSifre  # Burada '==' yerine '=' kullanılması gerekiyordu.
        print("Şifre başarıyla değiştirildi")
    else:
        print("Eski şifre hatalı")

while True:
    kullaniciAdi = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    kullaniciIndeks = kullaniciIndeksi(kullaniciAdlari, kullaniciAdi)
    if kullaniciIndeks != -1 and sifre == kullaniciSifreleri[kullaniciIndeks]:
        print("Giriş başarılı")

        while True:
            print("\nATM Uygulamasına Hoş Geldiniz")
            print("1. Bakiye görüntüleme")
            print("2. Para çek")
            print("3. Para yatır")
            print("4. Şifre değiştir")
            print("5. Çıkış")

            secim = int(input("Lütfen yapmak istediğiniz işlemi seçiniz (1-5): "))

            if secim == 1:
                bakiyeGoruntule(kullaniciBakiyeleri, kullaniciIndeks)
            elif secim == 2:
                miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
                paraCek(kullaniciBakiyeleri, kullaniciIndeks, miktar)
            elif secim == 3:
                miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
                paraYatir(kullaniciBakiyeleri, kullaniciIndeks, miktar)
            elif secim == 4:
                eskiSifre = input("Eski şifrenizi giriniz: ")
                yeniSifre = input("Yeni şifrenizi giriniz: ")
                sifreDegistir(kullaniciSifreleri, kullaniciIndeks, eskiSifre, yeniSifre)
            elif secim == 5:
                print("Sistemden çıkış yapılıyor...")
                break
            else:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        break
    else:
        print("Kullanıcı adı veya şifre hatalı, tekrar deneyiniz...")
