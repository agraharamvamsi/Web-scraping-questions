import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

question_links = soup.find_all(class_='question-hyperlink')
for link in question_links:
    print(link.get_text())