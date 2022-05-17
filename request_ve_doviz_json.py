import requests

url = "http://api.fixer.io/latest?base="



birinci_doviz = input("Birinci Döviz : ")
ikinci_doviz = input("İkinci Döviz : ")



response = requests.get(url + birinci_doviz)
json_verisi = response.json()

print(json_verisi)