sayi = int(input("Sayı Giriniz"))
tam_bolenler = list()
toplam = 0
for i in range(1, sayi):
    if sayi % i == 0:
        tam_bolenler.append(i)
        toplam += i
print(toplam)

if toplam == sayi:
    print("Sayı Mükemmel")
else:
    print("Sayı Mükemmel Değil")

