"""

file = open("bilgiler.txt","a",encoding="utf-8")
file.write("İsmet Alper Koyun\n")
file.close()
"""
"""

file = open("bilgiler.txt","r",encoding="utf-8")

for i in file:
    print(i,end="")
file.close()

"""
"""
file = open("bilgiler.txt","r",encoding="utf-8")
icerik = file.read()
print("Dosyanın İçeriği : ")
print(icerik)
print("Dosyanın içeriği 2: ")
icerik2 = file.read()
print(icerik2)
"""
file = open("bilgiler.txt","r",encoding="utf-8")
liste = file.readlines()
print(liste)
file.close()





"""
try:
    file = open("bilgiler2.txt","r")
except:
    print("Dosya Bulunamadı")

"""