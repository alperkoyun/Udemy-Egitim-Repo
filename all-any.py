def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
liste1 = [True,False,True,False,True]


def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

print(all(liste1))