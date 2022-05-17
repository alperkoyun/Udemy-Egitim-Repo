"""

liste = ["345", "sadas", "324a", "14", "kemal","345", "sadas", "324a", "14", "kemal","345", "sadas", "324a", "14", "kemal"]

for x in liste:
    try:
        print(int(x))
    except ValueError:
        pass

"""
sayılar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,"a","b","b","c"]
tek_sayılar = []
çift_sayılar = []
"""
def ciftmitekmi():
    a = int(input("Sayıyı Girin : "))
    if a % 2 != 0:
        raise ValueError("Tek Sayı Girdiniz")
    else:
        print("Sayınız",a)
        return a
"""

for x in sayılar:
    try:
        if int(x) % 2 == 0:
                çift_sayılar.append(x)
        else:
                tek_sayılar.append(x)
    except ValueError:
        print("Sayı Bölünemiyor",str(x))


print(çift_sayılar)
print(tek_sayılar)

