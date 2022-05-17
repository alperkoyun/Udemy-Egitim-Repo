class yazilimci:

    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgilerigoster(self):
        print("""
        
        Yazılımcı Objesinin özellikleri
        
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Bildiği Diller : {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def zam_yap(self,zam_miktari):
        print("Zam Yapılıyor")
        self.maas += zam_miktari

    def dil_ekle(self,yeni_dil):
        print("Dil Ekleniyor")
        self.diller.append(yeni_dil)

Yazilimci = yazilimci("İsmet Alper","Koyun",12345,3500,["Pyhton","Java","C","Bildiği diller"])

print(Yazilimci.bilgilerigoster())