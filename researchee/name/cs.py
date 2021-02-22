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


            
            index = name.find('Dr.')
            if index != -1:
                name = name.replace("Dr.", "")

            index = name.find('Prof.')
            if index != -1:
                name = name.replace("Prof.", "")
                
            index = name.find('-Ing.')
            if index != -1:
                name = name.replace("-Ing.", "")
                
            index = name.find('Ing.')
            if index != -1:
                name = name.replace("Ing.", "")
                
            index = name.find('-ing.')
            if index != -1:
                name = name.replace("-ing.", "")
                
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

            index = name.find('-Math.')
            if index != -1:
                name = name.replace("-Math.", "")

            index = name.find('-Inf.')
            if index != -1:
                name = name.replace("-Inf.", "")
                
            index = name.find('-INF.')
            if index != -1:
                name = name.replace("-INF.", "")
                
            index = name.find('(Sekretariat)')
            if index != -1:
                name = name.replace("(Sekretariat)", "")
                
            index = name.find('MBA')
            if index != -1:
                name = name.replace("MBA", "")
                
            index = name.find('(FH)')
            if index != -1:
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


            name = name.replace('é','e')
            name = name.replace('ü','ue')
            name = name.replace('ö','oe')
            
            name = name.replace("\t", "").replace("\r", "").replace("\n", "")
            #print(professorship)
            #name = '_'.join(name.split(' '))
            #professorship[pro_id] = '_'.join(professorship[pro_id].split(' '))
            nameAndFaculty = name + '&' + pro_name[pro_id]
            name_list.append(nameAndFaculty)

        pro_id += 1
        
    return name_list
    
print(getNameFromInformatikDept())