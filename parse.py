import csv
import poschunking


content_text=" "


def fetchcontent():

    global content_text

    content_text= poschunking.contentextract()
    return content_text




def iteratecsv(keyword,url):
    #print(keyword)

    f = open(url, "r")
    reader1 = csv.reader(f)
    for row in reader1:
        if (row[0] == keyword):
            if (row[2] == "ad"):

               return "ok",row[0],row[1]

            else:
                print("non ad")


def parse(url):

    probable_keywords = ['sheets', 'led', 'bus']  # ------------------this line change with keywords
    probable_keywords.sort()
    probabilities = []

    for i in probable_keywords:

        ad, word, probability = iteratecsv(i,url)
        # print(ad,word, probability)
        if (ad == "ok"):
            probabilities.append((word, probability))
            # print(word,probability)

    probabilities.sort(key=lambda x: x[1])
    length = len(probabilities)
    ad_keywo=probabilities[length - 1]
    ad_keyword=ad_keywo[0]
    print(ad_keyword)
    createtweetsentence(ad_keyword)



def createtweetsentence(ad_keyword):
    #if ad_keyword in content_text:
    #    print("partyy")

    print("---------------------------------------")
    global content_text
    content_text=fetchcontent()

    pos = content_text.find(ad_keyword)
    #print("hello", pos)
    text_tweet_like=content_text[pos-170:pos+100]
    sentimental_analysis(text_tweet_like)



def sentimental_analysis(text_tweet_like):
    a=10



parse("/home/nikhilponnuru/Desktop/ad-non.csv")


