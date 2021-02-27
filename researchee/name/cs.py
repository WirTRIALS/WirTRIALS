#return value should be a list, each item is a string containing name, jobTitle(professor or researcher) and professorship, seperated by '&'

from bs4 import BeautifulSoup
import requests

def getNameFromInformatikDept():
    faculty_name = "Computer Science"
    pro_list = ["https://osg.informatik.tu-chemnitz.de/Staff/", "https://www.tu-chemnitz.de/informatik/DVS/professur/mitarbeiter.php", "https://www.tu-chemnitz.de/informatik/HomePages/GDV/professurinhaber.php", "https://www.tu-chemnitz.de/informatik/KI/staff/index.php.en", "https://www.tu-chemnitz.de/informatik/mi/team.php.en", "https://www.tu-chemnitz.de/informatik/PI/professur/mitarbeiter/index.php.en","https://www.tu-chemnitz.de/informatik/CAS/people/people.php.en", "https://www.tu-chemnitz.de/informatik/ST/professur/staff.php.en", "https://www.tu-chemnitz.de/informatik/ce/professur/staff.php.en",
    "https://vsr.informatik.tu-chemnitz.de/about/people/"]
    
    pro_name = ["Operating System", "Data Management Systems", "Computer Graphics and Visualization", "Artificial Intelligence", "Media Informatics", "Practical Computer Science", "Computer Architectures and Systems", "Software Engineering", "Computer Engineering", "Distributed and Self-organizing Systems"]

    name_list = []
    prof_name = []
    pro_id = 0
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        if pro_id == 0:
           prof_name = soup.find_all("h4", class_="fn")
        elif pro_id == 1 or pro_id == 8:
           prof_name = soup.find_all("div", class_="h4")
        elif pro_id == 2:
           prof_name = soup.find_all("h3", class_="linie")
        elif pro_id == 4:
           prof_name = soup.find_all("div", {'class': 'mitarbeiter'})
           prof_name = soup.find_all("h3")
        elif pro_id == 5:
           prof_name = soup.find_all("div", {'class': 'h4'})
        elif pro_id == 6:
           parents = soup.find_all("main", {'class': 'page-content'})
           for soup_item in parents:
               prof_name = soup_item.find_all("p")
        elif pro_id == 7:
            prof_name = soup.find_all("div", class_="h4")
        else:
           prof_name = soup.find_all("h4", class_="fn")

        for item in prof_name:
            try:
                name = item.find("a").get_text()
            except:
                name = item.get_text()

            name = name.replace("Dr.", "")
            name = name.replace("Prof.", "")
            name = name.replace("-Ing.", "")
            name = name.replace("Ing.", "")
            name = name.replace("-ing.", "")
            name = name.replace("habil.", "")
            name = name.replace("nat.", "")
            name = name.replace("M.Sc.", "")
            name = name.replace("Dipl.", "")
            name = name.replace("-Math.", "")
            name = name.replace("-Inf.", "")
            name = name.replace("-INF.", "")
            name = name.replace("(Sekretariat)", "")
            name = name.replace("MBA", "")
            name = name.replace("(FH)", "")
                
            name = name.lstrip()
            name = name.strip()
            
            #old version of normalizing text

            '''index = name.find('Dr.')
            if index != -1:
                name = name[index + 4:]
                    
            index = name.find('Ing.')
            if index != -1:
                name = name[index + 5:]
            
            index = name.find('habil.')
            if index != -1:
                name = name[index + 7:]
            
            index = name.find('nat.')
            if index != -1:
                name = name[index + 5:]
            
            index = name.find('M.Sc.')
            if index != -1:
                name = name[index + 6:]'''

            
            name = name.replace("\t", "").replace("\r", "").replace("\n", "")
            #print(professorship)
            #name = '_'.join(name.split(' '))
            #professorship[pro_id] = '_'.join(professorship[pro_id].split(' '))
            nameAndFaculty = name + '&' + pro_name[pro_id] + '&' + faculty_name
            if nameAndFaculty not in name_list:
                name_list.append(nameAndFaculty)

        pro_id += 1
        
    return name_list
    
#print(getNameFromInformatikDept())