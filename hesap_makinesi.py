import matematik

print("""
*******************************************
İşlemler

1 - Toplama İşlemi

2 - Çıkarma İşlemi

3 - Çarpma İşlemi

4 - Bölme İşlemi

5 - Üste Yuvarla

6 - Faktoriyel Bul

7 - Kalanı Göster

8 - EBOB

9 - Karekokunu Bul

Kapatmak İçin Q ya basınız
**********************************************""")

while True:
    islem = int(input("İşlemi Giriniz :"))
    if islem == 5:
        sayi1 = float(input("Sayıyı Giriniz : "))
        if islem == 5:
            print("Yuvarlanmış Sayı : ", matematik.uste_yuvarla(sayi1))
    elif islem == 6 or islem == 9:
        sayi1 = int(input("Sayıyı Giriniz : "))
        if islem == 6:
            print("Faktoriyel : ", matematik.faktoriyel(sayi1))
        else:
            print("Karekök : ", matematik.karekok(sayi1))

    elif islem == 1 or islem == 2 or islem == 3 or islem == 4 or islem == 7 or islem == 8:
        sayi1 = int(input("1. sayıyı giriniz : "))
        sayi2 = int(input("2. Sayıyı giriniz : "))
        if islem == 1:
            print("Sayıların Toplamı : ", matematik.toplama(sayi1, sayi2))
        elif islem == 2:
            print("Çıkarma : ", matematik.cikarma(sayi1, sayi2))
        elif islem == 3:
            print("Çarpma : ", matematik.carpma(sayi1, sayi2))
        elif islem == 4:
            print("Bölme : ", matematik.bolme(sayi1, sayi2))
        elif islem == 7:
            print("Kalan : ", matematik.kalan(sayi1, sayi2))
        elif islem == 8:
            print("EBOB : ", matematik.ebob(sayi1, sayi2))
    else:
        break
