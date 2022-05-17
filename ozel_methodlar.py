class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("init Fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı : {}\nTürü: {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür)
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("Kitap Objesi siliniyor.....")

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") ## __init__methodu

print(kitap)
print(len(kitap))
del kitap