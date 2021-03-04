#return value should be a list, each item is a string containing name, jobTitle(professor or researcher) and professorship, seperated by '&'

from bs4 import BeautifulSoup
import requests

def getNameFromETITDept():
    faculty_name = "Electrical Engineering and Information Technology"
    pro_list = ["https://www.tu-chemnitz.de/etit/dst/professur/team.php.en", "https://www.tu-chemnitz.de/etit/ema/professur/team.php", "https://www.tu-chemnitz.de/etit/leb/staff/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/eneho/mitarbeiter/index.html", "https://www.tu-chemnitz.de/etit/hftet/professur/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/kn/team/index.php.en", "https://www.tu-chemnitz.de/etit/le/Professur/Mitarbeiter/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/nano/members.php", "https://www.tu-chemnitz.de/etit/messtech/team_e.php", "https://www.tu-chemnitz.de/etit/microsys/professur/mitarbeiter.php", "https://www.tu-chemnitz.de/etit/nt/mitarbeiter/index.php.en", "https://www.tu-chemnitz.de/etit/proaut/en/team.html", "https://www.tu-chemnitz.de/etit/control/team/index.php.en", "https://www.tu-chemnitz.de/etit/robosys/professorship/team.php.en", "https://www.tu-chemnitz.de/etit/sse/Mitarbeiter/index.html.en", "https://www.tu-chemnitz.de/etit/microtec/professur/mitarbeiter.php.en", "https://www.tu-chemnitz.de/etit/wetel/professur/mitarbeiter.php.en"]
    
    pro_name = ["Digital Signal Processing and Circuit Technology", "Electrical Energy Conversion Systems and Drives", "Electronic Components", "Power Systems and High-Voltage Engineering", "Microwave Engineering and Electromagnetic Theory", "Communication Networks", "Power Electronics", "Materials for Nanoelectronics", "Electrical Measurements and Sensor Technology", "Microsystems and Biomedical Engineering", "Communications Engineering", "Process Automation", "Automatic Control and System Dynamics", "Robotics and Human-Machine Interaction", "Circuit and System Design", "Smart Systems Integration", "Materials and Reliability of Microsystems"]
    
    
    name_list = []
    prof_name = []
<<<<<<< HEAD
    pro_id = 13
=======
    pro_id = 0
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')

        if pro_id == 2 or pro_id == 5:
            prof_name = soup.find_all("b")
        elif pro_id == 6 or pro_id == 14:
            prof_name = soup.find_all("a", class_ = "collapsed")
        elif pro_id == 10:
            prof_name = soup.find_all("h3", class_ = 'teaser')
        elif pro_id == 12:
<<<<<<< HEAD
            prof_name = []
=======
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
            table_list = soup.find_all("table")
            for table in table_list:
                prof_name.append(table.find("h3", {'style': 'margin:0;'}))
        elif pro_id == 13:
<<<<<<< HEAD
            prof_name = []
=======
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
            table_list = soup.find_all("div", class_ = "TeamTableCol")
            for table in table_list:
                prof_name.append(table.find("strong"))
        elif pro_id == 15:
<<<<<<< HEAD
            prof_name = []
            row_list = soup.find_all("tr")
            for row in row_list:
                if row.find("td"):
                    temp = row.find_all("td")[0].text.split(',')
                    
                    prof_name.append(temp[1]+ ' ' + temp[0])

=======
            row_list = soup.find_all("tr")
            for row in row_list:
                if row.find("td"):
                    prof_name.append(row.find_all("td")[0])
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
        else:
            prof_name = soup.find_all("div", class_ = "h4")
        

        for item in prof_name:
            try:
                name = item.find("a").get_text()
            except:
<<<<<<< HEAD
                try:
                    name = item.get_text()
                except:
                    name = item
                
=======
                name = item.get_text()
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176

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
            name = name.replace("MSc.", "")   
            name = name.replace("M.", "")
            name = name.replace("Sc.", "")
            name = name.replace("Sci.", "")   
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
            name = name.replace(",", "")                
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
<<<<<<< HEAD
        break

    return name_list
'''
list = getNameFromETITDept()
for item in list:
    print(item.split('&')[0] + '\t' + item.split('&')[1] + '\t' + item.split('&')[2])
'''
=======
    print(name_list)

    return name_list

getNameFromETITDept()

'''list = getNameFromETITDept()
for item in list:
    print(item.split('&')[0] + '\t' + item.split('&')[1])'''
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
