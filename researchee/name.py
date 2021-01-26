from bs4 import BeautifulSoup
import requests
<<<<<<< HEAD

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

def getAllName():

    name_list = []
    i = 0;
    while i < 8:
        name_list += getName(i)
        
#getName()
=======
import name
import re


def getName():
    faculty_list = ["naturwissenschaften/professuren.html", "informatik/professuren.php", "mathematik/professuren/prof.de.php",
                    "wirtschaft/fakultaet/professuren.php", "mb/professuren.php", "phil/professuren.php", "etit/profs/index.php", "hsw/professuren/index.php"]
    index = 0
    name_list = {"data": []}  # dictionary
    for f in faculty_list:
        r = requests.get('https://www.tu-chemnitz.de/'+f)
        soup = BeautifulSoup(r.text, 'html.parser')
        prof_list = soup.find_all("ul", class_="tucal-proflist")
        for li in prof_list:
            items = li.find_all("li")
            for item in items:
                prof = {}
                prof["name"] = item.find("span").contents[0]
                prof["professorship"] = item.find("strong").text
                if prof["name"][0] == 'N' and prof["name"][1] == '.':
                    continue
                index = index + 1
                prof["index"] = index
                name_list["data"].append(prof)

    return name_list
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df
