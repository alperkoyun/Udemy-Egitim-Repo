try:
    a = int(input("Sayı 1 :"))
    b = int(input("Sayı 2 :"))
    print(a/b)
except ValueError:
    print("Lütfen inputu doğru girin")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")
finally:
    print("burası çalıştı...")
print("Bloklar sona erdi")