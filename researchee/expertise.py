#This module contains a function, which could get all the expertises of a researher and store them into a json file.
#Function Name: getExpertise()
#Input: name_list.json
#Output: expertise_dict.json

from bs4 import BeautifulSoup
from requests import get
import random, time
import json

#get expertises of all names and store them into a json file
def getExpertise():
  
    input = open("name_list.json", "r", encoding='utf8') 
    json_object = input.read()
    name_list = json.loads(json_object)
    count = 0
    dict = {}
    for nameAndTitle in name_list:

        count += 1
        print(count)
        time.sleep(10)
        
        #print("***********************************")
        #print("***********************************")
        name = nameAndTitle.split('&')[0]
        str = getExpertiseFromMicrosoft(name)
        
        print(str)
        
        dict[nameAndTitle] = str
    
        
    json_object = json.dumps(dict, ensure_ascii=False) 
    with open("expertise_dict.json", "w", encoding='utf8') as outfile: 
        outfile.write(json_object)

    input.close()
    
#get one's expertises as well as the occurence each expertise has in his/her papers
def getExpertiseFromMicrosoft(name):
    
    tuc = 'chemnitz university of technology'
    headers = {'Ocp-Apim-Subscription-Key': '84b38efbbe4442c28184821a8a8b7795'}
    
    name = name.lower().replace('-',' ')
    name = name.replace('ä','a')
    name = name.replace('ö','o')
    name = name.replace('ü','u')
    name = name.replace('é','e')
    name = name.replace('ß','s')
    print(name)

    r = get('https://api.labs.cognitive.microsoft.com/academic/v1.0/calchistogram?expr=Composite(And(AA.AuN=\'' + name + '\',AA.AfN=\'' + tuc + '\'))&model=latest&attributes=F.FN&count=20&offset=0', headers = headers)
    #r = get('https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Composite(And(AA.AuN=\'' + name + '\',AA.AfN=\'' + tuc + '\'))&model=latest&attributes=F.FN,Ti,Y,CC,AA.AuN,DOI&count=20', headers = headers)

    #dict = json.loads(r.text)
    #print(dict)
    
    return r.text
    
    
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
            
            delay = 5 * random.random() + 5
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
    
#map expertise to WikiData
def mapToWikidata(expertise):

    API_ENDPOINT = "https://www.wikidata.org/w/api.php"

    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': expertise
    }

    r = get(API_ENDPOINT, params = params)

    url = 'http:' + r.json()['search'][0]['url']
    #print(url)
    return url
    
def readExpertise():
    input = open("expertise_dict.json", "r", encoding='utf8') 
    json_object = input.read()
    exp_dict = json.loads(json_object)
    for key in exp_dict.keys():
        exp = json.loads(exp_dict[key])
        print(exp['histograms'][0]['histogram'])
    #print(expertise_dict)
    '''
    for name in name_list:
        name = name.split('&')[0].strip()
        if name in list2:
            print(name)
        list2.add(name)
    print(len(list2))
    '''
    input.close()
    

#getExpertise()
mapToWikidata('Image processing')
#readExpertise()
#print(getExpertiseFromMicrosoft("Patrick Roßner"))