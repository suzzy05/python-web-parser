# Webpage Tools (Extractor + Simhash)

## Description

This repository contains two Python programs:

1. webpage_extractor.py  
   - Takes one URL  
   - Prints webpage title  
   - Prints full text  
   - Prints all links  

2. simhash_compare.py  
   - Takes two URLs  
   - Counts word frequency  
   - Computes 64-bit Simhash  
   - Prints number of common bits  

---

## Requirements

pip install requests  
pip install beautifulsoup4  

---

## How to Run

For Webpage Extractor:

python webpage_extractor.py https://example.com

For Simhash Comparison:

python simhash_compare.py https://www.google.com https://www.wikipedia.org

---

## Output

Extractor:
- Title
- Page text
- Links

Simhash:
- Number of common bits (out of 64)
