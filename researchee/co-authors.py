from bs4 import BeautifulSoup
import requests
# from flask import request, jsonify
# import name

def gettopCoauthor():
        r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
        soup = BeautifulSoup(r.text, 'html.parser')
        for data in soup.find_all('div', class_='gtm-coauthor-profile-item'):
            for a in data.find_all('a'):
                print(a.text) #for getting text between the link
       
# nova-e-link--theme-bare
def getPublication():
        r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
        soup = BeautifulSoup(r.text, 'html.parser')
        for data in soup.find_all('div', class_='nova-v-publication-item__title'):
            for a in data.find_all('a', class_='nova-e-link--theme-bare'):
                print(a.text) #for getting text between the link

# nova-v-publication-item__person-list
def getCoauthorForPublication():
        r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
        soup = BeautifulSoup(r.text, 'html.parser')
        for data in soup.find_all('ul', class_='nova-v-publication-item__person-list'):
            for a in data.find_all('a'):
                print(a.text) #for getting text between the link


getCoauthorForPublication()