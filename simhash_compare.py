import sys
import requests
from bs4 import BeautifulSoup

P = 53
M = 2**64

def word_hash(word):
    h = 0
    for i in range(len(word)):
        h = (h + ord(word[i]) * pow(P, i, M)) % M
    return h

def simhash(text):
    words = []

    for w in text.lower().split():
        clean = ""
        for c in w:
            if c.isalnum():
                clean += c
        if clean != "":
            words.append(clean)

    # manual frequency count
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    vector = [0] * 64

    for word in freq:
        h = word_hash(word)
        for i in range(64):
            if (h >> i) & 1:
                vector[i] += freq[word]
            else:
                vector[i] -= freq[word]

    result = 0
    for i in range(64):
        if vector[i] > 0:
            result |= (1 << i)

    return result

url1 = sys.argv[1]
url2 = sys.argv[2]

text1 = BeautifulSoup(requests.get(url1).text, "html.parser").get_text()
text2 = BeautifulSoup(requests.get(url2).text, "html.parser").get_text()

h1 = simhash(text1)
h2 = simhash(text2)

print("Simhash of URL1:", h1)
print("Simhash of URL2:", h2)


similarity = 64 - bin(h1 ^ h2).count("1")
print("Similarity (out of 64):", similarity)
