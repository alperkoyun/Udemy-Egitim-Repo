import math


def toplama(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    return sonuc


def cikarma(sayi1, sayi2):
    sonuc = sayi1 - sayi2
    return sonuc


def carpma(sayi1, sayi2):
    sonuc = sayi1 * sayi2
    return sonuc


def bolme(sayi1, sayi2):
    sonuc = sayi1 // sayi2
    return sonuc


def ebob(sayi1, sayi2):
    ebob = -1
    if sayi1 < sayi2:
        x = sayi1
    else:
        x = sayi2
    for i in range(1, x):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i
    sonuc = ebob
    return sonuc


def uste_yuvarla(sayi1):
    sonuc = int(sayi1+1)
    return sonuc


def faktoriyel(sayi1):
    faktoriyel = 1
    for x in range(1,sayi1+1):
        faktoriyel *= x
    sonuc = faktoriyel
    return sonuc


def karekok(sayi1):
    sonuc = sayi1**0.5
    return sonuc


def kalan(sayi1, sayi2):
    sonuc = sayi1 % sayi2
    return sonuc
