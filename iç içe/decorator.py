import time # decoratorsüz



def kareleri_hesapla(sayılar):
    sonuç = list()
    baslama = time.time()

    for i in sayılar:
        sonuç.append(i ** 2)
    bitis = time.time()
    print("Bu fonksiyon "+str(bitis-baslama) + "saniye sürdü")
    return sonuç
def küpleri_hesapla(sayılar):
    sonuç = list()
    baslama = time.time()
    for i in sayılar:
        sonuç.append(i ** 3)
    bitis = time.time()
    print("Bu fonksiyon "+str(bitis-baslama) + "saniye sürdü")
    return sonuç

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))



import time

def zaman_hesapla(func):
    def wrapper(sayılar):#deco
        baslama = time.time()

        sonuç = func(sayılar)

        bitis = time.time()

        print(func.__name__+" " + str(bitis-baslama) + "saniye sürdü.")
        return sonuç
    return wrapper
@zaman_hesapla # decoları kullanma bunu kullanmak istediğiniz fonksiyonunun üstüne yazılabilir
def kareleri_hesapla(sayılar):
    sonuç = list()

    for i in sayılar:
        sonuç.append(i ** 2)

    return sonuç
@zaman_hesapla #kod tekrarına düşmeden decoyla yazıldı
def küpleri_hesapla(sayılar):
    sonuç = list()

    for i in sayılar:
        sonuç.append(i ** 3)

    return sonuç

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))