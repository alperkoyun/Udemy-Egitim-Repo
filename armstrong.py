sayi = input("Sayı Giriniz :")

if len(sayi) == 4:
    toplam = 0
    for i in sayi:
        toplam += int(i) ** 4
    if toplam == int(sayi):
        print("Sayı Armstrong")
    else:
        print("Değil")
elif len(sayi) == 3:
    toplam = 0
    for i in sayi:
        toplam += int(i) ** 3
    if toplam == int(sayi):
        print("Sayı Armstrong")
    else:
        print("Değil")
else:
    print("İstenen formatta girmediniz...")


