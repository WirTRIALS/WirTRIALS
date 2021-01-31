#This module contains a function, which could get all the researchers' names of TUC.
#Function Name: getName()
#Parameters: empty
#Return Value: a list containing all the values

from bs4 import BeautifulSoup
import requests

def getName(facultyid):
    faculty_list = ["naturwissenschaften/professuren.html.en","informatik/professuren.php.en","mathematik/professuren/prof.en.php","wirtschaft/fakultaet/professuren.php.en","mb/professuren.php.en","phil/professuren.php.en","etit/profs/index.php.en","hsw/professuren/index.php.en"]
    faculty_name = ["Natural_Sciences","Computer_Science","Mathematics","Economic_and Business_Administration","Mechanical_Engineering","Humanities","Electrical_Engineering_and_Infomation_Technology","Behavioural_and_Social_Sciences"]
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

            index = professorship.find('Professorship')
            if index != -1:
                professorship = professorship[index+17:]
                
            name = '_'.join(name.split(' '))
            professorship = '_'.join(professorship.split(' '))
            
            #we append professorship and faculty to the name, seperated by &
            nameAndFaculty = name + '&' + professorship + '&' + faculty_name[facultyid]
            name_list.append(nameAndFaculty)


    return name_list


def getNameFromInformatikDept(faculty_id):
    faculty_name = "Computer_Science"
    faculty_list = ["https://osg.informatik.tu-chemnitz.de/Staff/", "https://www.tu-chemnitz.de/informatik/DVS/professur/mitarbeiter.php", "https://www.tu-chemnitz.de/informatik/HomePages/GDV/professurinhaber.php", "https://www.tu-chemnitz.de/informatik/KI/staff/index.php.en", "https://www.tu-chemnitz.de/informatik/mi/team.php.en"]
    professorship = ["Operating_System_Group", "Professur_Datenverwaltungssysteme", "Professorship of Computer Graphics and Visualization", "Professorship of Artificial Intelligence", "Professorship of Media Informatics"]
    name_list = []
    r = requests.get(faculty_list[faculty_id])
    soup = BeautifulSoup(r.text, 'html.parser')
    if faculty_id == 0:
       prof_name = soup.find_all("h4", class_="fn")
    elif faculty_id == 1:
       prof_name = soup.find_all("div", class_="h4")
    elif faculty_id == 2:
       prof_name = soup.find_all("h3", class_="linie")
    elif faculty_id == 4:
       prof_name = soup.find_all("div", {'class': 'mitarbeiter'})
       prof_name = soup.find_all("h3")
    else:
       prof_name = soup.find_all("h4", class_="fn")

    for item in prof_name:
        try:
            name = item.find("a").get_text()
        except:
            name = item.get_text()

        name = name.lstrip()
        name = name.strip()
        index = name.find('Dr.')
        if index != -1:
            name = name.replace("Dr.", "")

        index = name.find('Prof.')
        if index != -1:
            name = name.replace("Prof.", "")

        index = name.find('Ing.')
        if index != -1:
            name = name.replace("Ing.", "")

        index = name.find('habil.')
        if index != -1:
            name = name.replace("habil.", "")

        index = name.find('nat.')
        if index != -1:
            name = name.replace("nat.", "")

        index = name.find('M.Sc.')
        if index != -1:
            name = name.replace("M.Sc.", "")

        index = name.find('Dipl.')
        if index != -1:
            name = name.replace("Dipl.", "")

        index = name.find('Math.')
        if index != -1:
            name = name.replace("Math.", "")

        index = name.find('Inf.')
        if index != -1:
            name = name.replace("Inf.", "")

        index = name.find('(Sekretariat)')
        if index != -1:
            name = name.replace("(Sekretariat)", "")

        # old version of normalizing text
        # if name[0] == 'N' and name[1] == '.':
        #     continue;
        # index = name.find('Dr.')
        # if index != -1:
        #     name = name[index + 4:]
        #
        # index = name.find('Ing.')
        # if index != -1:
        #     name = name[index + 5:]
        #
        # index = name.find('habil.')
        # if index != -1:
        #     name = name[index + 7:]
        #
        # index = name.find('nat.')
        # if index != -1:
        #     name = name[index + 5:]
        #
        # index = name.find('M.Sc.')
        # if index != -1:
        #     name = name[index + 6:]


        name = name.replace("\t", "").replace("\r", "").replace("\n", "")
        #print(professorship)
        name = '_'.join(name.split(' '))
        professorship[faculty_id] = '_'.join(professorship[faculty_id].split(' '))
        nameAndFaculty = name + '&' + professorship[faculty_id] + '&' + faculty_name
        name_list.append(nameAndFaculty)

    return name_list

def getAllName():
    name_list = []
    #fetching data from the homepage of departments
    i = 0
    while i < 8:
        name_list += getName(i)
        i=i+1

    #fetching data from
    # 1. Operating system
    # 2. Database Mangement System
    # 3. Professur Graphische Datenverarbeitung und Visualisierung
    # 4. Professorship of Artificial Intelligence .
    # 5. Professorship of Media Informatics

    i = 0
    while i<5:
      name_list += getNameFromInformatikDept(i)
      i=i+1

    return name_list
