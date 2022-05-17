from modul_insan import Insan,sarisin



caner = Insan("caner",185)
alper = sarisin("sarı","alper",187)

print(caner.boy,caner.isim)
print(alper.boy,alper.isim,alper.renk)


print(caner)
print(alper)


print(len(caner))

print(len(alper))


del caner
del alper



a = 1
b = "alper"
try:
    a+b

except Exception as e:
    print(e)
    try:
        int(b)+a
    except Exception as ex:
        print(ex)