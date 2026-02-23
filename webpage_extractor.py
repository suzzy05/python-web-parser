import sys
import requests
from bs4 import BeautifulSoup

try:
    url = sys.argv[1]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Print title
    if soup.title:
        print(soup.title.string)

    # Print body text
    print(soup.get_text())

    # Print all links
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)

except:
    print("Enter URL or Error while fetching page")
