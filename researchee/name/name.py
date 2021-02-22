#This module contains a function, which could get all the researchers' names of TUC.
#Function Name: getName()
#Parameters: empty
#Return Value: a list containing all the values

from bs4 import BeautifulSoup
import requests

def getName():
    faculty_addr_list = ["/naturwissenschaften/professuren.html.en","/informatik/professuren.php.en","/mathematik/professuren/prof.en.php","/wirtschaft/fakultaet/professuren.php.en","/mb/professuren.php.en","/phil/professuren.php.en","/etit/profs/index.php.en","/hsw/professuren/index.php.en"]
    faculty_name_list = ["Natural Sciences","Computer Science","Mathematics","Economic and Business Administration","Mechanical Engineering","Humanities","Electrical Engineering and Infomation Technology","Behavioural and Social Sciences"]

    name_list = []
    uni_addr = 'https://www.tu-chemnitz.de'
    
    faculty_id = 0;
    while faculty_id < len(faculty_addr_list):
        
        #only extract faculty of computer science
        if faculty_id != 1:
            faculty_id += 1
            continue
        
        prof_addr_list = []
        prof_name_list = []
        
        r = requests.get(uni_addr + faculty_addr_list[faculty_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        list = soup.find_all("ul", class_="tucal-proflist")
        for ul in list:
            list2 = ul.find_all("li")
            for li in list2:
                try:
                    prof_addr_list.append(li.find("a")['href'])
                    prof_name_list.append(li.find("a").string)

                except:
                    pass
        print(prof_name_list)
        
        prof_id = 0;
        while faculty_id < len(prof_addr_list):
            r = requests.get(prof_addr_list[prof_id])
            soup = BeautifulSoup(r.text, 'html.parser')
            list = soup.find("div", id="tucal-pagemenu").ol

            prof_id += 1
            
        faculty_id += 1
        '''if name[0] == 'N' and name[1] == '.' : 
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
                    
                name = '_'.join(name.split(' '))
                professorship = '_'.join(professorship.split(' '))
                
                #we append professorship and faculty to the name, seperated by &
                nameAndFaculty = name + '&' + professorship + '&' + faculty_name[facultyid]
                name_list.append(nameAndFaculty)


    return name_list
'''



def getProfessorName(facultyid):
    faculty_list = ["naturwissenschaften/professuren.html.en","informatik/professuren.php.en","mathematik/professuren/prof.en.php","wirtschaft/fakultaet/professuren.php.en","mb/professuren.php.en","phil/professuren.php.en","etit/profs/index.php.en","hsw/professuren/index.php.en"]
    faculty_name = ["Natural Sciences","Computer Science","Mathematics","Economic and Business Administration","Mechanical Engineering","Humanities","Electrical Engineering and Infomation Technology","Behavioural and Social Sciences"]
    name_list = []

    r = requests.get('https://www.tu-chemnitz.de/'+faculty_list[facultyid])
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

            name = name.replace('é','e')
            name = name.replace('ü','ue')
            name = name.replace('ö','oe')
           
            index = professorship.find('Professorship')
            if index != -1:
                professorship = professorship[index+17:]
                
            #name = '_'.join(name.split(' '))
            #professorship = '_'.join(professorship.split(' '))
            
            #we append professorship and faculty to the name, seperated by &
            nameAndFaculty = name + '&' + professorship + '&' + faculty_name[facultyid]
            name_list.append(nameAndFaculty)


    return name_list
    
def getAllName():
    name_list = []
    #fetching data from the homepage of departments
    '''i = 0
    while i < 8:
        name_list += getProfessorName(i)
        i=i+1'''
    name_list += getProfessorName(1)
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

    i = 0
    while i<10:
      name_list += getNameFromInformatikDept(i)
      i=i+1
    #name_list += getNameFromInformatikDept(9)
    return name_list
