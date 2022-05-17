class Hayvan:
    def __init__(self):
        self.isim = None
        self.boy = None
        self.kilo = None

    def tanimla(self):
        self.isim = input("Hayvanınızın İsmini Giriniz")
        self.boy = input("Hayvanınızın Boyunu Giriniz")
        self.kilo = input("Hayvanınızın Kilosunu Giriniz")

class Kopek(Hayvan):
    def __init__(self):
        Hayvan().tanimla()
        self.yasadigi_yer = None
        self.dil = None
        self.kosma = None
        self.yas = None

    def __str__(self):
        return "İsim : {}\nBoy : {}\nKilo : {}\nYasadigi Yer : {}\nDil : {}".format(self.isim, self.boy, self.kilo,
                                                                                    self.yasadigi_yer, self.dil)

    def tanimla(self):
        self.yas = input("Yaşını Giriniz :")
        self.kosma = int(input("Koşma Hızını Giriniz M/s :"))

    def konusma(self):
        print((self.dil + ' ') * 3)

    def gel(self):
        mesafe = int(input("Geleceği Mesafiyi belirtiniz (Metre Cinsinden)"))
        kosma_hizi = self.kosma
        gelis_zamani = mesafe // kosma_hizi
        return "Tam {} dk sonra yanınızda olacak ..".format(gelis_zamani)

    def __del__(self):
        print("Köpek bilgileri siliniyor")


class Kus(Hayvan):
    def __init__(self, isim, boy, kilo, kanat_boyu, ucma_mesafesi, ucma_hizi):
        super().__init__(isim, boy, kilo)
        self.kanat_boyu = kanat_boyu
        self.ucma_mesafesi = ucma_mesafesi
        self.ucma_hizi = ucma_hizi

    def uc(self):
        mesafe = int(input("Geleceği Mesafiyi belirtiniz (Metre Cinsinden)"))
        ucma_hizi = self.ucma_hizi
        gelis_zamani = mesafe // ucma_hizi
        return "Tam {} dk sonra yanınızda olacak ..".format(gelis_zamani)

    def tanimla(self):
        self.kanat_boyu = input("Kanat boyunu Giriniz :")
        self.ucma_mesafesi = int(input("Uçma Mesafesini Giriniz M :"))
        self.ucma_hizi = int(input("Koşma Hızını Giriniz M/s :"))

    def __del__(self):
        print("Kuş bilgileri siliniyor")

    def __str__(self):
        return "İsim : {}\nBoy : {}\nKilo : {}\nKanat Boyu : {}\nUçma Mesafesi : {} cm\nUçma Hızı : {} M/s".format(
            self.isim, self.boy, self.kilo, self.kanat_boyu, self.ucma_mesafesi, self.ucma_hizi)


class At(Hayvan):
    def __init__(self, isim, boy, kilo, bacak_boyu, kosma_mesafesi, kosma_hizi):
        super().__init__(isim, boy, kilo)
        self.bacak_boyu = bacak_boyu
        self.kosma_mesafesi = kosma_mesafesi
        self.kosma_hizi = kosma_hizi

    def tanimla(self):
        self.bacak_boyu = input("Kanat boyunu Giriniz :")
        self.kosma_mesafesi = int(input("Uçma Mesafesini Giriniz M :"))
        self.kosma_hizi = int(input("Koşma Hızını Giriniz M/s :"))

    def __del__(self):
        print("At bilgileri siliniyor")

    def __str__(self):
        return "İsim : {}\nBoy : {}\nKilo : {}\nBacak Boyu : {} cm\nKoşma Mesafesi : {} M\nKoşma Hızı : {} M/s".format(
            self.isim, self.boy, self.kilo, self.bacak_boyu, self.kosma_mesafesi, self.kosma_hizi)


print("""

Hayvanlar Alemi Programı

Tanımlama yapmak için aşağıdaki seçeneklerden devam edebilirsiniz....

1 - Köpekler

2 - Kuşlar 

3 - Atlar

Çıkmak İçin 'q' ya basabilirsiniz.....
""")

while True:

    islem = input("Seçenek : ")

    if islem == "1":
        print("Köpek Tanımlama bilgilerini giriniz")
        kopek = Kopek()
        print(kopek)
    elif islem == "2":
        print("Kuş Tanımlama Bilgilerini Giriniz")
        print(Kus)
    elif islem == "3":
        print("At Tanımlama Bilgilerini Giriniz")
        print(At)
    else:
        print("Yanlış İşlem Yapıldı")
        break
