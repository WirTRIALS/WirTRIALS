#return value should be a list, each item is a string containing name, jobTitle(professor or researcher) and professorship, seperated by '&'

from bs4 import BeautifulSoup
import requests

def getNameFromETITDept():
    faculty_name = "Electrical Engineering and Information Technology"
    pro_list = ["https://www.tu-chemnitz.de/etit/dst/professur/team.php.en", "https://www.tu-chemnitz.de/etit/ema/professur/team.php", "https://www.tu-chemnitz.de/etit/leb/staff/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/eneho/mitarbeiter/index.html", "https://www.tu-chemnitz.de/etit/hftet/professur/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/kn/team/index.php.en", "https://www.tu-chemnitz.de/etit/le/Professur/Mitarbeiter/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/nano/members.php"]
    pro_name = ["Digital Signal Processing and Circuit Technology", "Electrical Energy Conversion Systems and Drives", "Electronic Components", "Power Systems and High-Voltage Engineering", "Microwave Engineering and Electromagnetic Theory", "Communication Networks", "Power Electronics", "Materials for Nanoelectronics"]
    
    
    name_list = []
    prof_name = []
    pro_id = 7
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        if pro_id == 0 or pro_id == 1 or pro_id == 3 or pro_id == 4 or pro_id == 7:
           prof_name = soup.find_all("div", class_ = "h4")
        elif pro_id == 2 or pro_id == 5:
           prof_name = soup.find_all("b")
        elif pro_id == 6:
           prof_name = soup.find_all("a", class_ = "collapsed")
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
            prof_name = soup.find_all("div", class_ = "h4")
        else:
           prof_name = soup.find_all("h4", class_ = "fn")


        for item in prof_name:
            try:
                name = item.find("a").get_text()
            except:
                name = item.get_text()

            if name.find("Secretariat") >= 0 or name.find("Frau") >= 0:
                continue 
            
            title = "researcher"
            if name.find("Prof.") >= 0:
                title = "professor"
            
            name = name.replace("Dr.", "")
            name = name.replace("Prof.", "")
            name = name.replace("-Ing.", "")
            name = name.replace("Ing.", "")
            name = name.replace("-Ing", "")
            name = name.replace("-ing.", "")
            name = name.replace("Eng.", "")
            name = name.replace("habil.", "")
            name = name.replace("nat.", "")
            name = name.replace("rer.", "")
            name = name.replace("h.c.", "")
            name = name.replace("M.", "")
            name = name.replace("Sc.", "")   
            name = name.replace("B.", "")
            name = name.replace("A.", "")               
            name = name.replace("Ph.D.", "")
            name = name.replace("Dipl.", "")
            name = name.replace("-Math.", "")
            name = name.replace("-Inf.", "")
            name = name.replace("-INF.", "")
            name = name.replace("MBA", "")
            name = name.replace("Herr", "")
            name = name.replace("(FH)", "")
            name = name.replace("(BA)", "")                
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
                name = name[index + 6:]


            name = name.replace('é','e')
            name = name.replace('ü','ue')
            name = name.replace('ö','oe')'''
            
            name = name.replace("\t", "").replace("\r", "").replace("\n", "")
            #print(professorship)
            #name = '_'.join(name.split(' '))
            #professorship[pro_id] = '_'.join(professorship[pro_id].split(' '))
            nameAndFaculty = name + '&' + title + '&' + pro_name[pro_id]
            name_list.append(nameAndFaculty)

        pro_id += 1
        
    return name_list
    
print(getNameFromETITDept())