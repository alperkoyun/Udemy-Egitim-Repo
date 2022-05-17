class Bilgisayar:

    def __init__(self, marka, surum, islemci, anakart, ram_miktari, ekran_karti):
        self.marka = marka
        self.surum = surum
        self.islemci = islemci
        self.anakart = anakart
        self.ram_miktari = ram_miktari
        self.ekran_karti = ekran_karti

    def __str__(self):
        return "Bilgisayar Bilgileri :\nMarka: {}\nSürüm: {}\nİşlemci: {}\nAnakart: {}\nRAM : {}\nEkran Kartı : {}".format(self.marka, self.surum, self.islemci, self.anakart, self.ram_miktari, self.ekran_karti)

bilgisayar = Bilgisayar("ASUS", "Windows 10", "I9 10700K", "Z170-A", "16", "RTX 3090")

print(bilgisayar)
