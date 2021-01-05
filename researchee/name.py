#This module contains a function, which could get all the researchers' names of TUC.
#Function Name: getName()
#Parameters: empty
#Return Value: a list containing all the values

from bs4 import BeauifulSoup
import requests

def getName():
    faculty_list = ["naturwissenschaften/professuren.html","informatik/professuren.php","mathematik/professuren/prof.de.php","wirtschaft/fakultaet/professuren.php","mb/professuren.php","phil/professuren.php","etit/profs/index.php","hsw/professuren/index.php"]
    name_list = []
    for f in faculty_list:
        r = requests.get('https://www.tu-chemnitz.de/'+f)
        soup = BeautifulSoup(r.text, 'html.parser')
        prof_list = soup.find_all("ul",class_="tucal-proflist")
        for li in prof_list:
            items = li.find_all("li")
            for item in items:
                name = item.find("span").contents[0]
                if name[0] == 'N' and name[1] == '.' : 
                    continue;
                name_list.append(name)

    return name_list
