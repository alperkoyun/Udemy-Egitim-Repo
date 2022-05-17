"""
def anafonksiyon(işlem_adı):

    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def çarpım(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım
    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpım
fonk = anafonksiyon("toplama")
fonk2 = anafonksiyon("çarpma")

print(fonk2(1,2,3,4,5))

"""



def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a*b
def bölme(a,b):
    return a/b

def anafonksiyon(func1,func2,func3,func4,işlem_adı):
    if işlem_adı == "toplama":
        print(func1(3,4))
    elif işlem_adı == "çıkarma":
        print(func2(10,3))
    elif işlem_adı == "çarpma":
        print(func3(3,5))
    elif işlem_adı == "bölme":
        print(func4(10,4))
    else:
        print("Geçersiz işlem ......")

anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme")
