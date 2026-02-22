import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Enter URL")
    sys.exit()

url = sys.argv[1]

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Print title
    if soup.title:
        print(soup.title.string)

    # Print body text
    text = soup.get_text()
    print(text)

    # Print all links
    links = soup.find_all("a")

    for link in links:
        href = link.get("href")
        if href:
            print(href)

except:
    print("Error while fetching page")