#append methodu en sona eleman eklemeye yarar

liste = [1,2,3,4,5]

liste.append(6)
print(liste)

#extend() bir listeye başka listenin elemanlarını ekler

liste1 = [1,2,3,4,5,6,7]
liste2 = [10,20,30]

liste1.extend(liste2)

print(liste1)


#insert methodu belli bir endekse eleman ekler silmez kaydırır

liste3 = [1,2,3,4,5,6,7,8,9]

liste3.insert(2,"Pyhton")

print(liste3)

#pop methodu içine değer vermezsek sondakini siler indeks değerine göre siler

liste4 = [1,2,3,4,5,6,7]

#liste4.pop(0)

print(liste4)

#remove methodu listeden eleman siler yazılan elemanı siler


liste5 = ["Pyhton","PHP","Java","C"]

#liste5.remove("pyhton")

#index methodu değer neredeyse baştan arayarak hangi indexte olduğunu söyler yoksa hata döner

liste6 = [1,2,3,4,3,3,5,6,7,8,9]

print(liste6.index(3))

print(liste6.index(3,3)) # belirli indexten başlatılıpta aranabilir


#count methodu verilen değerin kaç defa geçtiğini sayar

print(liste6.count(3))

#sort methodu elemanları sayıysa küçükten büyüğe string ise alfabetik sıralar reverse = True
# değeri verilirse tersten düzenler

liste7 = [12,-2,3,1,34,100]

print(liste7.sort()) # yazdırılamaz düzenler listeyi yazdırınca gözükür

print(liste7)

liste7.sort(reverse= True)

print(liste7)


