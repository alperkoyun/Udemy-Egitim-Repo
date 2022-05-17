liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste3 = ["python","php","java","javascript"]
i = 0
sonuc = list()
while i < len(liste1) and len(liste2):
    sonuc.append((liste1[i],liste2[i]))
    i += 1
print(sonuc)

print(list(zip(liste1,liste2,liste3)))