#from bs4 import BeautifulSoup
#from urllib.request import urlopen as uReq
import json

dictOfHashes = {}

# Opening of json file 
with open('trending.json') as tikTokFile:


    data = json.load(tikTokFile)

    for id in data['collector']:

        if len(id['hashtags']) > 0:

            for i in id['hashtags']:

                hashtag = i['name']

                if hashtag in dictOfHashes:

                    dictOfHashes[hashtag] += 1

                else:

                    dictOfHashes[hashtag] = 1


# Algorithm to sort the dictionary of hashtags by values
sortedValues = sorted(dictOfHashes.values(), reverse=True)
sortedDict = {}

for value in sortedValues:

    for key in dictOfHashes.keys():

        if dictOfHashes[key] == value:
            
            sortedDict[key] = dictOfHashes[key]

# Algorithm to make sure all the values were sorted correctly
for i in dictOfHashes.keys():
    if dictOfHashes[i] != sortedDict[i]:

        print("ERROR ERROR ERROR")
                
# Opening of file rankings to write the data too
newFile = open("rankings.txt", "w")

rankingCount = 1

for ranking in sortedDict.keys():

    newFile.write(str(rankingCount) + ". " + ranking + ": " + str(sortedDict[ranking]) + "\n")

    rankingCount += 1

newFile.close()






















"""
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

"""

linkCount = 10

for i in range(0, linkCount):

    mainClient = uReq('https://www.tiktok.com/en')

    htmlPage = mainClient.read()

    mainClient.close()

    soupObject = BeautifulSoup(htmlPage, "html.parser")

    containers = soupObject.findAll(attrs={"class":"tiktok-1itcwxg-ImgPoster e1yey0rl1"})

    print()
    print(containers)

"""