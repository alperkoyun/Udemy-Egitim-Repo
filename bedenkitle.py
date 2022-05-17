kilo = int(input("Kilonuzu girin "))
boy = float(input("Boyunuzu girin"))

beden_kitle_endeks = kilo/(boy*boy)

if beden_kitle_endeks < 18.5:
    print("Zayıf")
elif beden_kitle_endeks <25 and beden_kitle_endeks >= 18.5:
    print("Normal")
elif beden_kitle_endeks <30 and beden_kitle_endeks >=25:
    print("Fazla Kilolu")
else:
    print("obez")
    print(beden_kitle_endeks)