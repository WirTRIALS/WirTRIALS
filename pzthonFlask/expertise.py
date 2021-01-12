from bs4 import BeautifulSoup
import requests
from flask import request, jsonify
# import name

# def getExpertiseOfAllNameList():
#     namelistAuthors = name.getName()

#     for nl in namelistAuthors:
        
#         r = requests.get('https://www.researchgate.net/profile/'+nl)
#         expertList = []
#         soup = BeautifulSoup(r.text, 'html.parser')
#         mydivs = soup.findAll("a", {"class": "profile-about__badge"})        
#         for title in mydivs:
#             expertList.append(title.get_text())

#         if len(expertList)!=0:
#             print(nl)
#             print(expertList)


def getExpertise(name):
        r = requests.get('https://www.researchgate.net/profile/'+ str(name))
        expertList = []
        soup = BeautifulSoup(r.text, 'html.parser')
        mydivs = soup.findAll("a", {"class": "item__title"})        
        for title in mydivs:
            expertList.append(title.get_text())

        return expertList


# def inputFullname():
#     fullname = input("Enter Fullname:(For example: Martin_Gaedke) ")
#     expertlistOfName = getExpertise(fullname)
#     print(expertlistOfName)
# # print(getExpertise('Andre_Langer'))

# # inputFullname()