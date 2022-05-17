class Hayvan():
    def __init__(self):
        self.isim = None
        self.boy = None
        self.kilo = None
    def __str__(self):

        return "Hayvan bilgileri {} {} cm {} kg ".format(self.isim,self.boy,self.kilo)
    def tanimla(self):
        self.isim = input("ismi girin")
        self.boy = input("Boy girin")
        self.kilo = input("Kilo Girin")
class Kopek(Hayvan):
    def __init__(self):
        super().__init__()
        self.ayak_sayisi = None
        self.yas = None
        self.renk = None
    def __str__(self):
        return "Kopek bilgileri {}{}{}{}{}{}".format(self.isim,self.boy,self.kilo,self.ayak_sayisi,self.yas,self.renk)
    def tanimla(self):
        super().tanimla()
        self.ayak_sayisi = input("Ayak Sayısı")
        self.yas = input("Yaşını girin")
        self.renk = input("Rengini girin")



class goldenkopek(Kopek):
    def __init__(self):
        super().__init__()
        self.kafa = None
    def tanimla(self):
        super().tanimla()
        self.kafa = input("kafa girin")
    def __str__(self):
        return super().__str__()+"kafa : {} ".format(self.kafa)


golden = goldenkopek()
golden.tanimla()
print(golden)
"""
return "Golden Kopek bilgileri {} - {} - {} - {} - {} - {} - {} ".format(self.isim, self.boy, self.kilo,
                                                                         self.ayak_sayisi, self.yas,
                                                                         self.renk, self.kafa)
"""