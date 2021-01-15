from bs4 import BeautifulSoup
import requests
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
