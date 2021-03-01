#This module contains a function, which could get all the researchers' names of TUC.
#Function Name: getName()
#Parameters: empty
#Return Value: a list containing all the values

from bs4 import BeautifulSoup
import requests
from name.cs import getNameFromIFDept
from name.etit import getNameFromETITDept
from name.hsw import getNameFromHSWDept

def getProfessorName():
    faculty_list = ["naturwissenschaften/professuren.html.en","mathematik/professuren/prof.en.php","wirtschaft/fakultaet/professuren.php.en","mb/professuren.php.en","phil/professuren.php.en","etit/profs/index.php.en","hsw/professuren/index.php.en"]
    
    faculty_name = ["Natural Sciences","Mathematics","Economic and Business Administration","Mechanical Engineering","Humanities","Electrical Engineering and Infomation Technology","Behavioural and Social Sciences"]
    name_list = []

    faculty_id = 0
    while faculty_id < len(faculty_list):
        r = requests.get('https://www.tu-chemnitz.de/'+faculty_list[faculty_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        prof_list = soup.find_all("ul",class_="tucal-proflist")
        for li in prof_list:
            items = li.find_all("li")
            for item in items:
                name = item.find("span").contents[0]

                try:
                    professorship = item.find("a").get_text()
                except:
                    professorship = item.find("strong").contents[0]

                if name[0] == 'N' and name[1] == '.' : 
                    continue;
                index = name.find('Dr.')
                if index != -1:
                    name = name[index+4:]
                index = name.find('Ing.')
                if index != -1:
                    name = name[index+5:]
                index = name.find('habil.')
                if index != -1:
                    name = name[index+7:]
                index = name.find('nat.')
                if index != -1:
                    name = name[index+5:]

               
                index = professorship.find('Professorship')
                if index != -1:
                    professorship = professorship[index+17:]
                    
                #name = '_'.join(name.split(' '))
                #professorship = '_'.join(professorship.split(' '))
                
                #we append professorship and faculty to the name, seperated by &
                nameAndFaculty = name + '&professor' + '&' + professorship 
                name_list.append(nameAndFaculty)
                
        faculty_id += 1

    return name_list
    
'''
name_list = getProfessorName()
for name in name_list:
    print(name.split('&')[0] + '\t' + name.split('&')[1] + '\t' + name.split('&')[2])
'''


def getName():
    name_list = []
    #fetching data from the homepage of departments

    #fetching data from
    # 1. Operating system
    # 2. Database Mangement System
    # 3. Professur Graphische Datenverarbeitung und Visualisierung
    # 4. Professorship of Artificial Intelligence .
    # 5. Professorship of Media Informatics
    # 6. Professorship of Practical Computer Science
    # 7. Computer Architectures and Systems
    # 8. Software Engineering
    # 9. Computer Engineering
    # 10.Distributed and Self-organizing Systems


    #name_list += getNameFromIFDept()
    name_list += getNameFromETITDept()
    #name_list += getNameFromHSWDept()
    
    #wait to add other faculty's name lists
    '''
    professor_list = getProfessorName()
    for name in professor_list:
        if name not in name_list:
            name_list.append(name)
        else:
            print(name)
    '''
    return name_list

'''
name_list = getName()
count = 0
for name in name_list:
    count += 1
    print(str(count) + "\t" + name)
'''


# for get co workers
def coWorker():
    coworker_list = ["chemie/anorg/mitarbeiter.php.en",  "physik/CHEMPHYS/mitglieder.php", "chemie/tech/mitarbeiter.php.en",
                     "chemie/mc/public/mitarbeiter.php.en" , "chemie/physchem/index.html#mitarbeiter" , "chemie/elchem/seiten/mitarbeiter.php.en" , "chemie/polymer/aksommer/mitarbeiter.php.en"
                   ]
    name_list = []
    for f in coworker_list:
        r = requests.get('https://www.tu-chemnitz.de/'+f)
        soup = BeautifulSoup(r.text, 'html.parser')

        worker_list = soup.find_all("tr")
        if f != "chemie/physchem/index.html#mitarbeiter":
            for li in worker_list:
                if (len(li.find_all("td")) > 0):
                    td = li.find_all("td")[0]
                    if (td.find("a") != None):
                        name = td.contents[0].contents[0]
                        if (name != "Visiting scientists"):
                            if hasattr(name, 'contents'):
                                name_list.append(name.contents[0].text)
                            else:
                                name_list.append(name)

                    elif td.contents != None and td.contents[0] != " ":
                        name_list.append(td.contents)

        worker_list = soup.find_all("figure",class_="tucal-vcard")
        for li in worker_list:
            if (len(li.find_all("figcaption")) > 0):
                cap = li.find_all("figcaption")[0]
                if (len(cap.find_all("div",class_="h4")) > 0):
                    divs = cap.find_all("div",class_="h4")
                    name = divs[0].contents[0]
                    name_list.append(name)
    # coWorker_chemi()
    return name_list


def coWorker_chemi():
    coworker_list = ["chemie/org/mitarbeiter.html.en"]
    name_list = []
    for f in coworker_list:
        r = requests.get('https://www.tu-chemnitz.de/'+f)
        soup = BeautifulSoup(r.text, 'html.parser')

        worker_list = soup.find_all("div", {"class": ["mitarbeiter1", "mitarbeiter3"]})
        for li in worker_list:
            if (len(li.find_all("div")) > 0):
                divs = li.find_all("div")
                for div in divs:
                    if div.contents[0].find("<") == -1:
                        if div.contents != None and div.contents[0] != " ":
                            name_list.append(div.contents[0])

                    if(len(div.find_all("a")) > 0):
                        a = div.find_all("a")[0]
                        span = a.find("span")
                        if (span != None and (len(span.contents)) > 0):
                           name_list.append(span.contents[0])
                    if(len(div.find_all("div")) >0 ):
                        divv = div.find_all("div")
                        print (divv.contents)
                ps= li.find_all("p")
                for p in ps:
                    if(len(p.find_all("a")) > 0):
                        a = p.find_all("a")[0]
                        name_list.append(a.contents[0])
                aas = li.find_all("a")
                for a in aas:
                     if(len(a.find_all("span")) > 0):
                         span = a.find_all("span")[0]
                         name_list.append(span.contents[0])
    return name_list