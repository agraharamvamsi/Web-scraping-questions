import requests
from bs4 import BeautifulSoup
r = requests.get('https://stackoverflow.com/questions/tagged/python')
soup = BeautifulSoup(r.content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))