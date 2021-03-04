#return value should be a list, each item is a string containing name, jobTitle(professor or researcher) and professorship, seperated by '&'

from bs4 import BeautifulSoup
import requests

def getNameFromHSWDept():
    faculty_name = "Behavioural and Social Sciences"
    pro_list = ["https://www.tu-chemnitz.de/hsw/ab/prof/bewegungswissenschaft/professur/team.php", "https://www.tu-chemnitz.de/hsw/ab/prof/forschungsmethoden/professur/team.php", "https://www.tu-chemnitz.de/hsw/ab/prof/sportmedizin/professur/team.php.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/allpsy2/Professur/mitarbeiter.php.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/allpsy1/professur/team.php.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/geropsy/team.html.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/owpsy/Team/professur.php.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/method/index.html.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/klinpsy/team/mitarbeiter/index.php.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/ppd/professur/team/index.php.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/entwpsy/team/mitarbeiter.html.en", "https://www.tu-chemnitz.de/hsw/psychologie/professuren/sozpsy/professur/team.php", "https://www.tu-chemnitz.de/hsw/soziologie/Professuren/Epidemiologie/Professur/team.php", "https://www.tu-chemnitz.de/hsw/soziologie/Professuren/Techniksoziologie/Professur/team.php.en", "https://www.tu-chemnitz.de/hsw/soziologie/Professuren/Arbeit_und_Organisation/Professur/team.php.en", "https://www.tu-chemnitz.de/hsw/soziologie/Professuren/Empirische_Sozialforschung/Professur/team.php.en", "https://www.tu-chemnitz.de/hsw/soziologie/Professuren/Gesundheitssoziologie/Professur/team.php.en", "https://www.tu-chemnitz.de/hsw/soziologie/Professuren/Soziologische_Theorien/Professur/team.php"]
    
    pro_name = ["Human Locomotion", "Research Methodology and Data Analysis in Biomechanics", "Sports Medicine / Sports Biology", "General Psychology and Biopsychology", "Cognitive Psychology and Human Factors", "Applied Gerontopsychology and Cognition", "Work and Organizational Psychology", "Research Methods and Evaluation", "Clinicial Psychology", "Personality Psychology and Assessment", "Educational and Developmental Psychology", "Social Psychology", "Epidemiology", "Sociology of Technology with Specialization in Internet and New Media", "Sociology with Specialization in Work and Organization", "Sociology with Specialization in Empirical Social Research", "Sociology with Specialization in Health Research", "Sociological Theory"]
    
    
    name_list = []
    prof_name = []
    pro_id = 0
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')

        if pro_id == 7:
            prof_name = soup.find_all("div", class_ = "grid-item")

        else:
            prof_name = soup.find_all("div", class_ = "h4")
        

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
            name = name.replace("Jun.", "") 
            name = name.replace("-Prof.", "")
            name = name.replace("Prof.", "")
            name = name.replace("-Soz.", "")
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
            name = name.replace("-Psych.", "")
            name = name.replace("Psych.", "")
            name = name.replace("-PÃ¤d.", "")

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

    return name_list

'''list = getNameFromHSWDept()
for item in list:
    print(item.split('&')[0] + '\t' + item.split('&')[1])'''