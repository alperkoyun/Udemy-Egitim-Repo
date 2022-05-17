"""
def fonksiyon(*args): # demet oluşturur
    for i in args:
        print(i)

print(fonksiyon(1,2,3))


def fonksiyon(isim,*args):
    print("İsim:",isim)

    print("-------------")

    for i in args:
        print(i)

print(fonksiyon("Murat",1,2,3,4,5,6,7))


def fonksiyon(**kwargs): #isimli argümanlar dicts sözlük oluşturur
    print(kwargs)

print(fonksiyon( isim= "Murat",soyisim = "Coşkun",numara=12345))


def fonksiyon(*args, **kwargs): # ikisi beraber çağıralabilir
    for i in args:
        print(i)

    print("-----------------")

    for i,j in kwargs.items():
        print(i,j)

print(fonksiyon(1,2,3,4,5,6,7, isim= "Murat",soyisim = "Coşkun",numara=12345))


def selamla(isim):
    print("Selam ",isim)
print(selamla("alper"))

merhaba = selamla

merhaba("kemal")

def fonksiyon(): # fonksiyon içinde fonksiyon tanımlanabilir

    def fonksiyon2(): # local değer dışarıdan çağıralamaz
        print("Küçük fonksiyondan herkese merhaba")
    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")
print(fonksiyon())

"""

def fonksiyon(*args):

    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))
print(fonksiyon(1,2,3,4,5,6,7))
