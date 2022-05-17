from datetime import datetime
import locale #türkçe yapmak için

locale.setlocale(locale.LC_ALL,"") # BOŞ BIRAKIRSAK BULUNDUĞUMUZ BÖLGEYE GÖRE ALIR


su_an = datetime.now()

print(su_an.year)


print(datetime.ctime(su_an))



# yıl ay gün saat bilgisi almak


print(datetime.strftime(su_an,"%Y")) #YIL ALMAK İÇİN %Y TIRNAK İÇİNE
print(datetime.strftime(su_an,"%B")) #AY BİLGİSİNİ ALMAK İÇİN %B
print(datetime.strftime(su_an,"%D")) # GÜN BİLGİSİ ALMAKİÇİN
print(datetime.strftime(su_an,"%B %Y")) #AY VE YILI SADECE ALMAK İÇİN
#İNGİLİZCE GÖSTERİM İÇİN
# DİĞER GÖSTERİMLER İÇİN https://docs.python.org/2/library/time.html


# TİMESTAMP VE FROMTİMESTAMP FONKSİYONU

saniye = datetime.timestamp(su_an)
print(saniye)

su_an2 = datetime.fromtimestamp(saniye)

print(su_an2)