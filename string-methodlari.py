print("Pyhton".upper())# upper hepsini büyük harf yapar

print("PYHTON".lower())# hepsi küçük

print("Herkes ana baba bacı gardaş".replace("a","o"))# ilk değeri 2. değer olarak bütün stringte değiştirir

print("Python".startswith("P")) # p ile başlıyorsa true başlamıyorsa false döndürür büyük küçük farkeder

print("Pyhton".endswith("on")) # on ile bitiyorsa true bitmiyorsa false değeri döndürür büyük küçük farkeder

liste = "Pyhton Programlama Dili".split(" ") # her bir elemanı içeride belirtilen kurala göre boşluk - gibi listeye atar
print(liste)

print("                           python                              ".strip()) # komple bütün boşluğu siler bişey gönderilmezse
#   .lstrip soldaki boşlukları veya işaretleri siler
#    .rstrip sağdaki boşlukları siler

liste2 = ["21","02","2014"]  # join methodu bütün elemanların arasına girecek elemanı yazılır listeyi değiştirmez
print("/".join(liste2))
print(liste2)

print("ada kapısı yandan çarklı".count("a",2))  # .count kaçtane geçtiğini sayar içerideki değerin 2. değerde index girilebilirde girmeye bilirde


print("araba".find("a")) # hangi indexte bulunduğunu söyler ilk bulduğu indexi döndürür -1 değeri döndürür

print("araba".rfind("a")) # sondan arar .rfind sondan sayıp hangi değerdeyse onu söyler olmadı -1 değeri döndürür