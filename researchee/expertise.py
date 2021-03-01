#This module contains a function, which could get all the expertises of a researher.
#Function Name: getExpertiseFromResearchgate(),getExpertiseFromSpringer()
#Parameters: a string which contains researcher's name
#Return Value: a list containing all the expertises of the researcher

from bs4 import BeautifulSoup
import requests
import name
import random, time
    


def getExpertise(name):

    '''
    delay = 5 * random.random() + 5
    time.sleep(delay)
    print("after " + str(delay) + " seconds, now extracting " + name)
    '''    
    expertList = []
    expertList += getExpertiseFromResearchgate(name)
    #expertList += getExpertiseFromSpringer(name)
    #expertList += getExpertiseFromGooglescholar(name)

    return expertList

def getExpertiseFromResearchgate(name):
    
    tuc = "Chemnitz"
    name = '-'.join(name.split(' '))
    name = name.replace('é','e')
    name = name.replace('ü','ue')
    name = name.replace('ö','oe')
    name = name.replace('ä','ae')
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'}
    
    count = 1
    flag = 0
    while count <= 2 or flag == 0:
        try:
            
            delay = 10 * random.random() + 10
            time.sleep(delay)
            print("after " + str(delay) + " seconds, now extracting " + name)
            
            if count == 1:
                #print('https://www.researchgate.net/profile/'+name)
                r = requests.get('https://www.researchgate.net/profile/'+name)
                #print(r.text)
            else:
                r = requests.get('https://www.researchgate.net/profile/'+name + '-' + str(count))

            expertList = []
            soup = BeautifulSoup(r.text, 'html.parser')

            try:
                if soup.find("h3").text.startswith("Please,"):
                    return ["stop"]
            except:
                pass
             
            institution = soup.find("div", {"class": "nova-e-text nova-e-text--size-m nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-grey-600"}).find("span").find("span").text
            print(institution)
            
            if institution.find(tuc) == -1:
                count += 1
                continue
            
            mydivs = soup.findAll("a", {"class": "profile-about__badge"})

            for title in mydivs:
                exp = title.get_text()
                expertList.append(exp)
            
            print(expertList)
            return expertList
        except:
            print("no expertise in researchGate")
            flag = 1
        count += 1
            
    return []    


def getExpertiseFromSpringer(name):
    try:
        r = requests.get('https://link.springer.com/search/facetexpanded/sub-discipline?facet-creator=' + name + '&showAll=true')

        expertList = []
        soup = BeautifulSoup(r.text, 'html.parser')

        subs = soup.findAll("span",class_="facet-title")        
        for sub in subs:
            exp = sub.get_text()
            expertList.append(exp)
        #print("springer: " + expertList)
        return expertList
    except:
        print("no expertise in springer")
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
        
def getExpertiseFromPublons(name):
    try:
        headers = { "Authorization":"Token 021cf3835d6b66f2b435f6a51090f3b0ad0a74e0",
        "Content-Type": "application/json"}
        r = requests.get("https://publons.com/api/v2/academic/" + name, headers = headers)
        
        print(r.text)
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

    
#getExpertiseFromResearchgate("Martin Gaedke")