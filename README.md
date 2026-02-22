# Python Web Page Extractor

## Description
This project is a simple Python program that takes a URL, fetches the web page, and prints:

- Page Title
- Page Body Text (without HTML tags)
- All URLs present in the page

It uses the `requests` library to fetch the webpage and `BeautifulSoup` to parse HTML content.

---

## Requirements

Make sure Python is installed.

Install required libraries:

pip install requests
pip install beautifulsoup4

---

## How to Run

Open terminal in project folder and run:

python script.py

(Currently the URL is hardcoded inside the script.)

You can change the URL inside the file:
url = "https://www.google.com"

---

## Output

The program prints:

1. Title of the webpage
2. Complete text content of the webpage
3. All links (href values) found inside `<a>` tags

---

## Shilpi Shaw
