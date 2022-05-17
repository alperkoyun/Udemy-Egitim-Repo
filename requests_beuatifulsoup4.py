import requests
from bs4 import  BeautifulSoup
url = "https://firmadan.com/"
response = requests.get(url)


print(response)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

#print(soup.prettify())

#for i in soup.find_all("h1"):
 #   print(i.get("href"))
  #  print("*********************************")

#print(soup.find_all("a"))
for i in soup.find_all("div",{"class":"col-sm-6 col-md-3 col-6 px-12px col-xl-2 col-lg-2 col-md-3 pb-3"}):
    print(i)
    print("**************")