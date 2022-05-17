def nothesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1*(3/10) + not2 * (3/10) + not3 * (4/10)
    if son_not >= 90:
        harf = "AA"
    elif son_not >=85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"
    return isim + "------------------->" + harf + "\n"


with open("dosya.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        sonuc = nothesapla(i)
        eklenecekler_listesi.append(sonuc)
        if "FF" in sonuc:
            with open("kalanlar.txt","a",encoding="utf-8") as file2:
                file2.write(sonuc)
        else:
            with open("gecenler.txt","a",encoding="utf-8") as file3:
                file3.write(sonuc)

"""
       
        if "FF" in :
            with open("kalanlar.txt", "w", encoding="utf-8") as file2:
                file2.write
        else:
            with open("gecenler.txt","a",encoding="utf-8") as file3:
                file3.write

"""









"""
with open("notlar.txt","w",encoding="utf-8") as file2:
    for i in eklenecekler_listesi:
        print(i)
        file2.write(i)
with open("kalanlar.txt","w",encoding="utf-8") as file3:
    for x in eklenecekler_listesi:
        if "FF" in x :
            file3.write(x)
        else:
            with open("gecenler.txt","a",encoding="utf-8") as file4:
                file4.write(x)
                
                """