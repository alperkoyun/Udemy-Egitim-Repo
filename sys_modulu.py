import sys


"""
a = int(input("a:"))
b = int(input("b:"))

sys.exit() # programdan çıkmak için kullanılır alltaki komutlar kullanılamaz

c = int(input("c:"))
"""

#stderr ve stdout
#Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.

#stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.

#stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.

#stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.

sys.stderr.write("Bu bir hata mesajıdır\n") # hata mesajı olarak yazılabilir

sys.stderr.flush() # direk yazdırmak için bufferı silip direk yazdırıyor

sys.stdout.write("Bu normal bi yazıdır\n") #normal bi mesaj olarak yazılabilir


print(sys.argv) # bilgisayardaki yolunu gösterir liste olarak eklenir

for i in sys.argv:
    print(i)

