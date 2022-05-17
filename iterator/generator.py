def kareleri_al():
    for i in range(1,6):
        yield i**2
generator = kareleri_al()

iterator = iter(generator)

print(next(iterator))
print(next(iterator))

