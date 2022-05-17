class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan Sınıfının init fonksiyonu..")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş : {}\nDepartman : {}".format(self.isim,self.maaş,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman
class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişi_sayısı):
        super().__init__(isim,maaş,departman)

        self.kişi_sayısı = kişi_sayısı

    def bilgilerigöster(self):
        print("Yönetici sınıfının bilgileri.....")

        print("İsim : {} \nMaaş : {}\nDepartman : {}\nKişi Sayısı : {}".format(self.isim, self.maaş, self.departman,self.kişi_sayısı))

    def zam_yap(self,yeni_zam_miktarı):
        self.maaş += yeni_zam_miktarı

yönetici = Yönetici("İsmet Alper Koyun",3000,"Bilişim Departmanı",10)
yönetici.zam_yap(500)
print(yönetici.bilgilerigöster())