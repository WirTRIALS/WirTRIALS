from bs4 import BeautifulSoup
import requests
# from flask import request, jsonify
# import name

def gettopCoauthor():
        r = requests.get('https://www.researchgate.net/profile/Martin_Gaedke')
        soup = BeautifulSoup(r.text, 'html.parser')
        for data in soup.find_all('div', class_='js-target-experience-list'):
            for a in data.find_all('b'):
                print(a.text) #for getting text between the link
gettopCoauthor()
