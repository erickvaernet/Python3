
# https://www.youtube.com/watch?v=rhnMvvmfBFI
from bs4 import BeautifulSoup
import requests


url = "https://www.clarin.com/"

response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

# cap_apotheosis = soup.body.div['app'].find("header")

# cap_apotheosis = soup.body.div.app.pb-5()

# cap_apotheosis = soup.body.div.app.pb-5()

titulares_h1 = soup.find_all("h1")
titulares_h2 = soup.find_all("h2")
titulares_h3 = soup.find_all("h3")

for titulo in titulares_h1:
    print(titulo)


for titulo2 in titulares_h2:
    print(titulo2)

for titulo3 in titulares_h3:
    print(titulo3)
