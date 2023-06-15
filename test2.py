import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the question links on the page
question_links = soup.find_all('a', class_='question-hyperlink')

# Print the text of each question
for link in question_links:
    print(link.text.strip())
