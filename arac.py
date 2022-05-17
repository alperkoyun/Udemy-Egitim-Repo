class Araba():
    def __init__(self,model,renk,beygir_gucu,silindir):
        print("init fonksiyonu çağırıldı")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir

araba1 = Araba("Renault Megane","Gümüş",110,4)

araba2 = Araba("Peugeot","Beyaz",90,4)

print(araba1.model,araba2.model)