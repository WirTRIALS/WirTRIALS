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

    return expertise_list
