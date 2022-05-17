import os
from datetime import datetime

#os.chdir("C:/Users/FeyzAlp/Desktop")   #dizini değiştirme
#print(os.getcwd()) # bulunduğu dizini söyler

#print(os.listdir()) # masaüstündeki dosya ve klasörlerin hepsini gösterir

#for i in os.listdir():
#    print(i)

# os.mkdir("Deneme1") #tek klasör oluşturma alt klasör oluşturulma yapılamıyor bu şekilde

# os.makedirs("Deneme1/deneme2/deneme3") # çoğul alt klasör oluşturmak için

# os.rmdir("Deneme1/deneme2") # remove klasör herhangi bir klasörü silmek

# os.removedirs("Deneme1/deneme2") # altklasörleri komple silmek

# os.rename("test.txt","test2.txt") # isim değiştirme

# print(os.stat("test2.txt")) # dosyanın özelliklerini verir

#print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) #datetime eklendi çünkü saniye cinsinden veriyordu çevirmek için stmtime değiştirilme maketime yani


#os.walk("C:/Users/FeyzAlp/Desktop") # generator objesi oluşturur itere edilebilir

#for i in os.walk("C:/Users/FeyzAlp/Desktop"): # bütün dosya ve klasörleri görmek
    #print(i) # her bir i değeri demet

#for klasor_yolu,klasor_isimleri,dosya_isimler in os.walk("C:/Users/FeyzAlp/Desktop"):

 #   print("Klasör Yolu",klasor_yolu)
  #  print("Klasör İsimler",klasor_isimleri)
   # print("Dosya isimleri",dosya_isimler)
    #print("***************************************************") # bütün dosyalar ve klasörleri i elemanı olarak yazdırdık

#sadece txt olanları almak için

#for klasor_yolu,klasor_isimleri,dosya_isimler in os.walk("C:/Users/FeyzAlp/Desktop"):
 #   for i in dosya_isimler:
  #      if i.endswith(".txt"):
   #         print(i)