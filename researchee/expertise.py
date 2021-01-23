#This module contains a function, which could get all the expertises of a researher.
#Function Name: getExpertise()
#Parameters: a string which contains researcher's name
#Return Value: a list containing all the expertises of the researcher

from bs4 import BeautifulSoup
import requests
import name

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


def getExpertise(name):
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

def getExpertiseDemo(name):
    list = ["web_engineering","software_engineering"]
    return list
    
def inputFullname():
    fullname = input("Enter Fullname:(For example: Martin_Gaedke) ")
    expertlistOfName = getExpertise(fullname)
    print(expertlistOfName)
    
#print(getExpertise('Martin_Gaedke'))
