toplam = 0
while True:
    sayi = input("Sayı giriniz (hepsini toplamak için q ya basınız")
    if sayi != "q":
        toplam += int(sayi)
    else:
        print(toplam)
        break
