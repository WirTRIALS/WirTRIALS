from bs4 import BeautifulSoup
import requests
# from flask import request, jsonify
# import name


def getImage(name):
    r = requests.get('https://www.researchgate.net/profile/'+name)
    soup = BeautifulSoup(r.text, 'html.parser')
    img = soup.find("img", {"class": "nova-e-avatar__img"})
    return str(img['src'])


def gettopCoauthor():
    r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
    soup = BeautifulSoup(r.text, 'html.parser')
    for data in soup.find_all('div', class_='gtm-coauthor-profile-item'):
        for a in data.find_all('a'):
            print(a.text)  # for getting text between the link

# nova-e-link--theme-bare


def getPublication(name):

    r = requests.get('https://www.researchgate.net/profile/'+name)
    soup = BeautifulSoup(r.text, 'html.parser')
    publications = {"data": []}

    for data in soup.find_all('div', class_='nova-v-publication-item__body'):
        pubs = {}
        coauthors = {"data": []}
        title = data.select(
            '.nova-v-publication-item__title .nova-e-link--theme-bare')
        coauthor = data.select(
            '.nova-v-publication-item__stack-item .nova-v-person-inline-item__fullname')

        published_date = data.select(
            '.nova-v-publication-item__stack-item .nova-v-publication-item__meta-right span')

        for data in coauthor:
            co = {}
            co["author"] = data.text
            coauthors["data"].append(co)

        pubs["title"] = title[0].text
        pubs["published_date"] = published_date[0].text
        pubs["coauthor"] = coauthors
        publications["data"].append(pubs)

    return publications
# for getting text between the link

# nova-v-publication-item__person-list


def getCoauthorForPublication():
    r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
    soup = BeautifulSoup(r.text, 'html.parser')
    for data in soup.find_all('ul', class_='nova-v-publication-item__person-list'):
        for a in data.find_all('a'):
            print(a.text)  # for getting text between the link
