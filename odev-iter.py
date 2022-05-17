class Kareler():


    def __init__(self,max = 0):

        self.max = max
        self.sayi = 0

    def __iter__(self):

        return self
    def __next__(self):
        if (self.sayi <= self.max):
            sonuc = self.sayi ** 2

            self.sayi += 1

            return sonuc
        else:
            self.sayi = 0
            raise StopIteration
iterator = iter(Kareler(7))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


