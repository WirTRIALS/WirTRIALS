from bs4 import BeautifulSoup
import requests
import name

def getExpertise():
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

getExpertise()