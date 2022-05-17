import sqlite3

import time

class Şarkı():

    def __init__(self,isim,sanatçı,albüm,prodüksiyon,süre):

        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon = prodüksiyon
        self.süre = süre

    def __str__(self):
        return "Kitap İsmi: {}\nŞarkı İsmi : {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon: {}\nSüre :\n".format(self.isim, self.sanatçı,
                                                                                          self.albüm, self.prodüksiyon,
                                                                                          self.süre)
class Liste():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("şarkı.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists Liste (şarkı_ismi TEXT,sanatçı TEXT,albüm TEXT,prodüksiyon TEXT,süre INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def şarkıları_goster(self):

        sorgu =  "Select * From Liste"

        self.cursor.execute(sorgu)

        Liste = self.cursor.fetchall()

        if (len(Liste) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in Liste:

                liste = Liste(i[0],i[1],i[2],i[3],i[4])
                print(liste)

    def kitap_ekle(self, Şarkı):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu, (Şarkı.isim, Şarkı.sanatçı, Şarkı.albüm , Şarkı.prodüksiyon,Şarkı.süre))

        self.baglanti.commit()
Liste.baglanti_olustur(Şarkı)