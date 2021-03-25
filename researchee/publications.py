# This module contains a function, which could get all the expertises of a researher and store them into a json file.
# Function Name: getPublications()
# Input: name_list.json
# Output: publication_dict.json

from bs4 import BeautifulSoup
from requests import get
import random, time
import json


# get expertises of all names and store them into a json file
def getPublications():
    input = open("name_list.json", "r", encoding='utf8')
    json_object = input.read()
    name_list = json.loads(json_object)
    count = 0
    dict = {}
    for nameAndTitle in name_list:
        count += 1
        print(count)
        time.sleep(10)

        # print("***********************************")
        # print("***********************************")
        name = nameAndTitle.split('&')[0]
        str = getPublicationsFromMicrosoft(name)

        print(str)

        dict[nameAndTitle] = str

    json_object = json.dumps(dict, ensure_ascii=False)
    with open("publications_dict.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)

    input.close()


# get one's publications as well as the occurence each expertise has in his/her papers
def getPublicationsFromMicrosoft(name):
    tuc = 'chemnitz university of technology'
    headers = {'Ocp-Apim-Subscription-Key': '97f6254b16834610995f63512ba79d7c'}

    name = name.lower().replace('-', ' ')
    name = name.replace('ä', 'a')
    name = name.replace('ö', 'o')
    name = name.replace('ü', 'u')
    name = name.replace('é', 'e')
    name = name.replace('ß', 's')
    print(name)


    r = get('https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Composite(And(AA.AuN=\'' + name + '\',AA.AfN=\'' + tuc + '\'))&model=latest&attributes=F.FN,Ti,Y,CC,AA.AuN,DOI&count=20', headers = headers)

    dict = json.loads(r.text)
    print(dict)

