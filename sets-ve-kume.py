


x = {1,2,3}
print(type(x))

x = set()

liste = [1,2,3,3,1,1,2,2,2] #

x2 = set(liste) # her bi elemandan bi tane alır stringler dahil
# süslü parantez
print(x2)


x3 = {"elma","armut","Kiraz","Muz"}
liste4 = list(x3)

print(liste4)

#for i in x3:
 #   print(i)

# kümenin elemanlarını for ile yada listeye çevirip yazdırabilinir index verilip yazdırılamaz

# add methodu

x5 = {1,2,3}

x5.add(4)

print(x5)

# bi daha add eklenirse eklenmez tek aynı isimde tek eleman olabilir

#------------------------------------------------------

# diffrence methodu

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

print(küme1.difference(küme2)) #küme 1 de olup küme 2 de olmayanları yazdırır


küme1.difference_update(küme2) # küme 2 de olanları silip küme 1 i günceller

print(küme1)
print(küme2)

# discard methodu  kümede olan elemanı silmeye yarar

küme2.discard(23)

print(küme2)

# intersection ortak olanları yazar
print(küme1.intersection_update(küme2)) # kesişim kümesini günceller olur

# isdisjoint() methodu iki kümenin ortak kümesi boşsa false varsa ortak true döner
küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

print(küme1.isdisjoint(küme2))


# issubset() alt kümesiyse true değilse false döner

print(küme1.issubset(küme2))

# union() metodu birleşim kümesini döner

print(küme1.union(küme2))

#update methodu

print(küme1.update(küme2))

