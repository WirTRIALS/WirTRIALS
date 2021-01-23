from bs4 import BeautifulSoup
import requests
import name
import re


def getName():
<<<<<<< HEAD
<<<<<<< HEAD
    faculty_list = ["naturwissenschaften/professuren.html","informatik/professuren.php","mathematik/professuren/prof.de.php","wirtschaft/fakultaet/professuren.php","mb/professuren.php","phil/professuren.php","etit/profs/index.php","hsw/professuren/index.php"]
    faculty_name = ["Natural_Sciences","Computer_Science","Mathematics","Economic_and Business_Administration","Mechanical_Engineering","Humanities","Electrical_Engineering_and_Infomation_Technology","Behavioural_and_Social_Sciences"]
    name_list = []
    i = 0
    while i < 8:
        r = requests.get('https://www.tu-chemnitz.de/'+faculty_list[i])
=======
=======
>>>>>>> b2e1249872c432d2e42e43dfb147e1be22c2579c
    faculty_list = ["naturwissenschaften/professuren.html", "informatik/professuren.php", "mathematik/professuren/prof.de.php",
                    "wirtschaft/fakultaet/professuren.php", "mb/professuren.php", "phil/professuren.php", "etit/profs/index.php", "hsw/professuren/index.php"]
    index = 0
    name_list = {"data": []}  # dictionary
    for f in faculty_list:
        r = requests.get('https://www.tu-chemnitz.de/'+f)
>>>>>>> b2e1249 (UI to show researchers profile, publications, expertise and co-authors. Bug fixes)
        soup = BeautifulSoup(r.text, 'html.parser')
        prof_list = soup.find_all("ul", class_="tucal-proflist")
        for li in prof_list:
            items = li.find_all("li")
            for item in items:
<<<<<<< HEAD
<<<<<<< HEAD
                name = item.find("span").contents[0]
                if name[0] == 'N' and name[1] == '.' : 
                    continue;
                fullname = name.split(' ')
                while fullname[0].startswith("Univ.") or fullname[0].startswith("Dr") or fullname[0].startswith("Prof.") or fullname[0].startswith("Jun."):
                    fullname.pop(0)
                name = '_'.join(fullname)
                nameAndFaculty = name + '&' + faculty_name[i]
                name_list.append(nameAndFaculty)
        i += 1   
    return name_list
#print(getName())
=======
=======
>>>>>>> b2e1249872c432d2e42e43dfb147e1be22c2579c
                prof = {}
                prof["name"] = item.find("span").contents[0]
                prof["professorship"] = item.find("strong").text
                if prof["name"][0] == 'N' and prof["name"][1] == '.':
                    continue
                index = index + 1
                prof["index"] = index
                name_list["data"].append(prof)

    return name_list
<<<<<<< HEAD
>>>>>>> b2e1249 (UI to show researchers profile, publications, expertise and co-authors. Bug fixes)
=======
>>>>>>> b2e1249872c432d2e42e43dfb147e1be22c2579c
