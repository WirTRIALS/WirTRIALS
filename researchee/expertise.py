from bs4 import BeautifulSoup
import requests


def getExpertise(name):
    r = requests.get('https://www.researchgate.net/profile/'+name)
    soup = BeautifulSoup(r.text, 'html.parser')
    expertise = soup.findAll("a", {"class": "profile-about__badge"})
    expertise_list = {"data": []}

    for i in expertise:
        ex = {}
        ex["expertise"] = i.get_text()
        expertise_list["data"].append(ex)

<<<<<<< HEAD
def getExpertiseDemo(name):
    list = ["web_engineering","software_engineering"]
    return list
    
def inputFullname():
    fullname = input("Enter Fullname:(For example: Martin_Gaedke) ")
    expertlistOfName = getExpertise(fullname)
    print(expertlistOfName)
    
#print(getExpertise('Martin_Gaedke'))
=======
    return expertise_list
>>>>>>> b2e1249 (UI to show researchers profile, publications, expertise and co-authors. Bug fixes)
