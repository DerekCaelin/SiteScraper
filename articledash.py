import requests
import csv
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0'}
sitelist = [
    #Motherboard
    "https://www.vice.com/en_us/section/tech",

    # Wired
    "https://www.wired.com/category/ideas/",
    
    #MIT Technology Review
    "https://www.technologyreview.com/",

    #The Verge / Technology
    "https://www.theverge.com/tech",

    # Slate / Technology
    "https://slate.com/technology",

    # The Atlantic / Technology
    "https://www.theatlantic.com/technology/",

    # OneZero
    "https://onezero.medium.com/"
]


# create csv file
with open('sitedata.csv', 'w',  newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Publication","Title","Description","URL"])

# the parent function for all functions
def Lookup(url):
    print("looking up "+url)
    page = requests.get(url, headers=headers)
    global soup
    soup = BeautifulSoup(page.text, "html.parser")

    # select which process to use, depending on the url
    ChooseSite(url)

# based off the url, choose a different scraping behavior
def ChooseSite(url):
    if url == "https://www.vice.com/en_us/section/tech":
        ScrapeType1(url)
    elif url == "https://www.wired.com/category/ideas/":
        ScrapeType2(url)
    elif url == "https://www.technologyreview.com/":
        ScrapeType3(url)
    elif url =="https://www.theverge.com/tech":
        ScrapeType2b(url)
    elif url =="https://slate.com/technology":
        ScrapeType4(url)
    elif url =="https://www.theatlantic.com/technology/":
        ScrapeType5(url)
    elif url =="https://onezero.medium.com/":
        ScrapeType6(url)
    else:
        print ("didn't recognize link.")

# Vice
def ScrapeType1(url):
    print("scraping "+url)
    chunk = soup.find_all("a", {"class": 'heading-hover'})
    for words in chunk:
        title = words.attrs['title']
        description = words.find("div", {"class": 'text-card__inner__dek'}).get_text()
        link = words.get('href')
        fullUrl = "https://vice.com"+link
        WriteCSV("Motherboard", title, description, fullUrl)

#Wired
def ScrapeType2(url):
    print("scraping "+url)
    chunk = soup.find_all("a",{"class":"post-listing-list-item__link"})

    #print(chunk)
    for words in chunk:
        #print(words)
        title = words.find("h5").get_text()
        link = words.get('href')
        fullUrl ="https://wired.com"+link
        WriteCSV("Wired", title, "", fullUrl)

# The Verge / Tech
def ScrapeType2b(url):
    print("scraping "+url)
    chunk = soup.find_all("div",{"class":"c-compact-river__entry "})

    #print(chunk)
    for words in chunk:
        title = words.get_text()
        link = words.find("a").get('href')
        fullUrl = "https://theverge.com"+link
        WriteCSV("The Verge / Technology", title, fullUrl,"")

#MIT Technology Review
def ScrapeType3(url):
    print("scraping "+url)
    chunk = soup.find_all("a",{"class":"teamModuleItem__postLink--1rmAi"})
    #chunk = soup.find_all(attrs={"class": "feedItem__wrapper--3w0Fq"}) popular--inFeed__story--1SJZb, infiniteItemList__wrapper--Y6jl0

    print(chunk)
    for words in chunk:
        title = words.get_text()
        #description = words.find("a",{"class":"popular__itemTitle--3oYx0"}).get_text()
        link = words.get('href')
        WriteCSV("MIT Technology Review", title, "", link)

#Slate / Technology
def ScrapeType4(url):
    print("scraping "+url)
#    chunk = soup.find_all("div", {"class": 'cards-component'},"h2")
    chunk = soup.find_all("a",{"class","topic-story"})

    #print(chunk)
    for words in chunk:
        title = words.find("span",{"class":"topic-story__hed"}).get_text().lstrip().rstrip()
        link = words.get("href")
        fullUrl = link
        WriteCSV("Slate / Technology", title, "", fullUrl)

# The Atlantic / Tech
def ScrapeType5(url):
    print("scraping "+url)
    chunk = soup.find_all("div", {"class": 'c-story__content c-story__content--left'})
    #print(chunk)
    for words in chunk:
        title = words.find("p",{"class":"c-story__title c-story__title--left o-hed"}).get_text()
        description = words.find("p", {"class": 'c-story__dek c-story__dek--left o-hed'}).get_text()
        link = words.find("a").get("href")
        fullUrl = link
        WriteCSV("The Atlantic / Technology", title, description, fullUrl)

# OneZero
def ScrapeType6(url):
    print("scraping "+url)
    chunk = soup.find_all("div", {"class": 'n fq p fr fs'})
    for words in chunk:
        #print(words)
        title = words.find("h2").get_text()
        description = words.find("h3").get_text()
        link = words.find("a").get('href')
        fullUrl = "https://onezero.medium.com"+link
        WriteCSV("OneZero", title, description, fullUrl)


def WriteCSV(pub, title, dek, url):
    with open('sitedata.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([pub, title, dek, url])
        print(title)
        print(dek)
        print(url)

def Analysis():
    a = 1

# The Beginning! Start the process
for site in sitelist:
    Lookup(site) #for each url in the list of urls, do the process
    Analysis()

