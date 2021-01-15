from bs4 import BeautifulSoup
import requests
# from flask import request, jsonify
# import name


def getImage(name):  # image prof. name ,organization, introduction
    r = requests.get('https://www.researchgate.net/profile/'+name)
    soup = BeautifulSoup(r.text, 'html.parser')

    img = soup.find("img", {"class": "nova-e-avatar__img"})
    name_list = {"data": []}
    prof = {}
    prof["img"] = img['src']
    prof["name"] = img['alt']

    try:
        org = soup.find("a", {"class": "gtm-institution-item"})
        prof["org"] = org.text
    except Exception as e:
        prof["org"] = ""

    try:
        about = soup.find("span", {"class": "Linkify"})
        prof["about"] = about.text
    except Exception as e:
        about = ""
        prof["about"] = about

    name_list["data"].append(prof)
    return name_list


def getDetails(name):  # image prof. name ,organization, introduction
    r = requests.get('https://www.researchgate.net/profile/'+name)
    soup = BeautifulSoup(r.text, 'html.parser')
    name_list = {"data": []}
    prof = {}

    designation = soup.find("div", {
                            "class": "nova-e-text nova-e-text--size-m nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-grey-600 title"})
    prof["desg"] = designation.text

    name_list["data"].append(prof)
    return name_list


def gettopCoauthor():
    r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
    soup = BeautifulSoup(r.text, 'html.parser')
    for data in soup.find_all('div', class_='gtm-coauthor-profile-item'):
        for a in data.find_all('a'):
            print(a.text)  # for getting text between the link

# nova-e-link--theme-bare


def getPublication():
    r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
    soup = BeautifulSoup(r.text, 'html.parser')
    for data in soup.find_all('div', class_='nova-v-publication-item__title'):
        for a in data.find_all('a', class_='nova-e-link--theme-bare'):
            print(a.text)  # for getting text between the link

# nova-v-publication-item__person-list


def getCoauthorForPublication():
    r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
    soup = BeautifulSoup(r.text, 'html.parser')
    for data in soup.find_all('ul', class_='nova-v-publication-item__person-list'):
        for a in data.find_all('a'):
            print(a.text)  # for getting text between the link
