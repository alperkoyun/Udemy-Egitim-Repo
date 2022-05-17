
"""
def asal_yazdir():

    sayi = list(range(2,1000))

    for i in sayi:
        print(i)





print(asal_yazdir())
"""

def ekstra(fonk):

    def wrapper(sayı):
        toplam = 0

        for i in range(1, sayı):

            if (sayı % i == 0):
                toplam += i

        return toplam == sayı

    for i in range(1, 1001):
        if (wrapper(i)):
            print("Mükemmel Sayı:", i)
    return fonk()

@ekstra
def asal_sayi():

    sayi1 = 1
    sayi2 = 1000

    print(sayi1, "ile", sayi2, "arasındaki asal sayılar:")

    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    break
            else:
                print(sayi)