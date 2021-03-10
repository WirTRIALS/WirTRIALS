from ldap3 import Server, Connection, SUBTREE, LEVEL
from string import ascii_lowercase
from itertools import product
import time
import json

def getNameFromHumanities():
    total_entries = 0
    connection_kwargs = {
        'server': 'ldap.tu-chemnitz.de',
        'auto_bind': True,
    }
    conn = Connection(**connection_kwargs)
    pause_counter = 0
    combos = (''.join(i) for i in product(ascii_lowercase, repeat = 3)) # Looping through characters a-z 
    for keyword in combos:
        pause_counter += 1
        entry_generator = conn.extend.standard.paged_search(search_base = 'ou=Users,dc=tu-chemnitz,dc=de',
                search_filter= '(& (objectClass=Person) (uid='+keyword+'*) (|(ou=*Fakultät für Wirtschaftswissenschaften*) (ou=*Philosophische Fakultät*) (ou=*Fakultät für Maschinenbau*)))',
                                                        search_scope = SUBTREE,
                                                        attributes = ['cn', 'ou', 'title','uid'],
                                                        paged_size= 200,
                                                        get_operational_attributes=True)  
        namelist = []


<<<<<<< HEAD
    for entry in entry_generator:
        total_entries += 1
        name = ''.join(entry['attributes']['cn'])
        faculty = "Economics"
        professorship = ''.join(entry['attributes']['ou'][0])
        professorship_ = professorship.split("|")[0]
        title = "Researcher"
        if ''.join(entry['attributes']['title']) == "Prof.":
            title = "Professor"
        #print(entry['attributes']['title'])
        nameAndFaculty = name + '&' + title + '&' + professorship_
        namelist.append(nameAndFaculty)
=======
        for entry in entry_generator:
            namse = ''.join(entry['attributes']['uid'])
            total_entries += 1
            name = ''.join(entry['attributes']['cn'])
            faculty = "Humanities"
            professorship = ''.join(entry['attributes']['ou'][0])
            professorship_ = professorship.split("|")[-1]
            title = "Researcher"
            if ''.join(entry['attributes']['title']) == "Prof.":
                title = "Professor"
            
            nameAndFaculty = name + '&' + title + '&' + professorship_
            namelist.append(nameAndFaculty)
        
        if pause_counter == 2:
            delay = 0.1
            time.sleep(delay)
            pause_counter = 0

    json_object = json.dumps(namelist) 

    with open("professor_names.json", "w") as outfile: 
        outfile.write(json_object) 
>>>>>>> 0625d940d9e9a8c5bb8218872775c235a5dc1109
    print(namelist)
    print(total_entries)
    return(namelist)

getNameFromHumanities()

