import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = 'https://clerk.house.gov/Votes/2023724'
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
div_content = soup.find('div', class_='table-responsive')

# Extract and print information from the table within the div
rows = div_content.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    print(row_data)
