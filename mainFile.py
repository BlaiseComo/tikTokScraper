from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

dictOfHashes = {}

mainClient = uReq('https://en.wikipedia.org/wiki/List_of_most-liked_TikTok_videos')

htmlPage = mainClient.read()

mainClient.close()

soupObject = BeautifulSoup(htmlPage, 'html.parser')

for link in soupObject.find_all('a'):

    linkString = str(link)

    print(link.get('href'))

    if len(linkString.split('@')) == 2:

        print(link.get('href'))






"""
for i in range(0, linkCount):

    mainClient = uReq('https://www.tiktok.com/en', )

    htmlPage = mainClient.read()

    mainClient.close()

    soupObject = BeautifulSoup(htmlPage, "html.parser")

    containers = soupObject.findAll(attrs={"class":"tiktok-1itcwxg-ImgPoster e1yey0rl1"})

    print()
    print(containers)

"""