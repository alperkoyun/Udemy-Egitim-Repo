sayi = range(1,100)
liste = list()
for i in sayi:
    if i % 3 != 0:
        continue
    else:
        liste.append(i)
        print(i)
print(liste)