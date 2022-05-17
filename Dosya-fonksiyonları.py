
"""
with open("bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())
    file.seek(5)
    print(file.tell())

    """
"""
with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik = file.read(10)
    file.seek(0)
    icerik2 = file.read(6)
    print(icerik)
    print(icerik2)

"""