liste1 = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]


def ucgen_mi(liste):
    ucgen_olanlar = list()
    ucgen_olmayanlar = list()
    for a, b, c in liste:
        if a + b > c and a + c > b and b + c > a:
            ucgen_olanlar.append((a,b,c))
        else:
            ucgen_olmayanlar.append((a, b, c))
    return ucgen_olanlar
print(ucgen_mi(liste1))
print(list(filter(ucgen_mi,liste1)))
"""
for a, b, c in liste1:
    print(a, b, c)
"""