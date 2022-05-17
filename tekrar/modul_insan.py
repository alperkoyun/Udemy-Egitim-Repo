class Insan():
    def __init__(self,isim,boy):
        self.isim = isim
        self.boy = boy


    def __str__(self):
        return "İsim : {}\nBoy : {}\n".format(self.isim,self.boy)


    def __len__(self):
        return self.boy

    def __del__(self):
        print(self.isim+" Siliniyor .........")

class sarisin(Insan):
    def __init__(self, renk, isim, boy):
        super().__init__(isim, boy)
        self.renk = renk


    def __str__(self):
        return "İsim : {}\nBoy : {}\nRenk : {}".format(self.isim,self.boy,self.renk)


    def __len__(self):
        return self.boy

    def __del__(self):
        print(self.isim+" Siliniyor .........")

