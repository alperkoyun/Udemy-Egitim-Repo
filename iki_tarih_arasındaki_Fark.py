from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

tarih = datetime(2019,12,1)

su_an = datetime.now()

print(su_an-tarih)