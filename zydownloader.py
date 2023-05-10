#!/usr/bin/python

import requests, json, os
from pprint import pprint


session = requests.Session()

with open("../zyinfo", "r") as info:
    book = info.readline()[0: -1]
    authToken = info.readline()[0: -1]

mainBookUrl = f"https://zyserver.zybooks.com/v1/zybooks?zybooks=[\"{book}\"]&auth_token={authToken}"

def getChapters():
    data = session.get(mainBookUrl).text
    data = json.loads(data)
    chapters = data['zybooks'][0]['chapters']
    return chapters


for chapter in getChapters():
    chapterNum = chapter['number']
#    os.mkdir(str(chapterNum))
    for section in chapter['sections']:
        sectionNum = section['number']

#        page = open(f"str(sectionNum)", 'w')

        pageUrl = f"https://zyserver.zybooks.com/v1/zybook/{book}/chapter/{chapterNum}/section/{sectionNum}?auth_token={authToken}"
        print(session.get(pageUrl).text)
