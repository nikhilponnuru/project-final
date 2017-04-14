
import urllib
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

content_text = ""

def contentextract():

    # def poschunking(url):
    # url = "https://ponnurunikhilkumar.wordpress.com/2016/04/12/compiler-extensions-like-chrome-extensions/"

    url = "https://ponnurunikhilkumar.wordpress.com/2016/04/12/compiler-extensions-like-chrome-extensions/"
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    content_text = text.encode('utf-8')

    return content_text


#print(content_text)


'''
word_tokens=word_tokenize(content_text)

stop_words=set(stopwords.words('english'))

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


print(filtered_sentence)
'''

#print(contentextract())


