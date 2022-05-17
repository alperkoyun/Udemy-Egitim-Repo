import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık") # Bütün bilgileri alıyoruz.
    data = cursor.fetchall() # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.
verileri_al()
con.close()