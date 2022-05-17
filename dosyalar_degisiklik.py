"""with open("bilgiler.txt","r+",encoding="utf-8") as file:
    file.seek(10)
    file.write("Deneme")
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read()) dosyada değişiklik"""



"""
with open("bilgiler.txt","a",encoding="utf-8") as file:
    file.write("Caner Koyun\n")

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read()) sonunda değişikliik yapmak """

"""
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
    icerik = "Mehmet keper\n" + icerik # başına ekleme kısmı
    print(icerik)
    file.seek(0) # önemli
    file.write(icerik) # önemli
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
"""
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"caner ke7\n") # ekleme işlemi
    file.seek(0) # enbaştaki satıra gittik
    file.writelines(liste)
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    icerik = file.read()
    print(icerik)
    """"
    
    for i in liste: # for döngüsüylede yazılabilir writelines ile de
        file.write(i) # dosyaya yazıcak for döngüsü
    print(liste)
     """


