kenarlar = ((3, 4), (10, 3), (5, 6), (1, 9))

"""
def hesapla(liste):
    d = 0
    alan = list()
    while d < len(liste):
        for i, j in liste:
            alan.append(i * j)
            d += 1
    return alan

"""
def hesap(liste):
    alan = list()
    for i, j in liste:
        alan.append(i*j)

    return alan

print(hesap(kenarlar))

