<<<<<<< HEAD
#This module contains a function, which could get all the expertises of a researher.
#Function Name: getExpertiseFromResearchgate(),getExpertiseFromSpringer()
#Parameters: a string which contains researcher's name
#Return Value: a list containing all the expertises of the researcher

from bs4 import BeautifulSoup
import requests
import name
import random, time

def getExpertiseOfAllNameList():
    namelistAuthors = name.getName()

    for nl in namelistAuthors:
        
        r = requests.get('https://www.researchgate.net/profile/'+nl)
        expertList = []
        soup = BeautifulSoup(r.text, 'html.parser')
        mydivs = soup.findAll("a", {"class": "profile-about__badge"})        
        for title in mydivs:
            expertList.append(title.get_text())

        if len(expertList)!=0:
            print(nl)
            print(expertList)
=======
from bs4 import BeautifulSoup
import requests
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df

def getExpertise(name):
<<<<<<< HEAD

    delay = 5 * random.random() + 5
    time.sleep(delay)
    print("after " + str(delay) + " seconds, now extracting " + name)
    
    expertList = []
    expertList += getExpertiseFromResearchgate(name)
    expertList += getExpertiseFromSpringer(name)
    expertList += getExpertiseFromGooglescholar(name)

    return expertList
    
def getExpertiseFromResearchgate(name):
    r = requests.get('https://www.researchgate.net/profile/'+name)
    # print(name)
    expertList = []
    soup = BeautifulSoup(r.text, 'html.parser')

    mydivs = soup.findAll("a", {"class": "profile-about__badge"})        
    for title in mydivs:
        exp = title.get_text()
        exp = '_'.join(exp.split(' '))
        expertList.append(exp)

    return expertList

def getExpertiseFromSpringer(name):
    try:
        r = requests.get('https://link.springer.com/search/facetexpanded/sub-discipline?facet-creator=' + name + '&showAll=true')

        expertList = []
        soup = BeautifulSoup(r.text, 'html.parser')

        subs = soup.findAll("span",class_="facet-title")        
        for sub in subs:
            exp = sub.get_text()
            exp = '_'.join(exp.split(' '))
            expertList.append(exp)
        return expertList
    except:
        return []

def getExpertiseFromGooglescholar(name):
    try:
        r = requests.get('https://scholar.google.de/citations?view_op=search_authors&mauthors=' + name)

        expertList = []
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup)
        subs = soup.findAll("a",class_="gs_ai_one_int")        
        for sub in subs:
            exp = sub.get_text()
            exp = '_'.join(exp.split(' '))
            expertList.append(exp)
        return expertList
    except:
        return []
        
def getExpertiseDemo(name):
    list = ["web_engineering","software_engineering"]
    return list
    
def inputFullname():
    fullname = input("Enter Fullname:(For example: Martin_Gaedke) ")
    expertlistOfName = getExpertise(fullname)
    print(expertlistOfName)
    

def test():
    namelist = name.getName()

    for n in namelist:
        n = n.split('&')[0]
        delay = 5 * random.random() + 5
        time.sleep(delay)
        print("----------expersise of " + n + " is: ---------------")
        print(getExpertiseFromGooglescholar(n))
        
        
#test()
=======
    r = requests.get('https://www.researchgate.net/profile/'+name)
    soup = BeautifulSoup(r.text, 'html.parser')
    expertise = soup.findAll("a", {"class": "profile-about__badge"})
    expertise_list = {"data": []}

    for i in expertise:
        ex = {}
        ex["expertise"] = i.get_text()
        expertise_list["data"].append(ex)

    return expertise_list
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df
