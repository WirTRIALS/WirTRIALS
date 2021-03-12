from ldap3 import Server, Connection, SUBTREE, LEVEL
from string import ascii_lowercase
from itertools import product
import time
import json

def getName():
    total_entries = 0
    connection_kwargs = {
        'server': 'ldap.tu-chemnitz.de',
        'auto_bind': True,
    }
    conn = Connection(**connection_kwargs)
    pause_counter = 0
    combos = (''.join(i) for i in product(ascii_lowercase, repeat = 3)) # Looping through characters a-z 
    namelist = []
    for keyword in combos:

        pause_counter += 1
        entry_generator = conn.extend.standard.paged_search(search_base = 'ou=Users,dc=tu-chemnitz,dc=de',
                search_filter= '(& (objectClass=Person)(uid='+keyword+'*)(&(ou=*Fakultät*)(ou=*Professur*)))',
                search_scope = SUBTREE,
                attributes = ['cn', 'ou', 'title','uid'],
                paged_size= 200,
                get_operational_attributes=True)  


        for entry in entry_generator:
            #namse = ''.join(entry['attributes']['uid'])
            total_entries += 1
            
            name = entry['attributes']['cn'][0]
            if len(entry['attributes']['cn'])>1:
                if name.isascii():
                    name = entry['attributes']['cn'][1]
                
            for faculty in entry['attributes']['ou']:
                if 'Fakult' in faculty and 'professur' in faculty.lower():
                    break
            
            #print(faculty)
            
            title = "Researcher"
            if "Prof." in ''.join(entry['attributes']['title']):
                title = "Professor"
            
            nameAndFaculty = name + '&' + title + '&' + faculty
            namelist.append(nameAndFaculty)
            print(nameAndFaculty)
            #print(entry)
        if pause_counter == 2:
            delay = 0.1
            time.sleep(delay)
            pause_counter = 0
        
    json_object = json.dumps(namelist, ensure_ascii=False) 
    
    with open("name_list.json", "w", encoding='utf8') as outfile: 
        outfile.write(json_object)
    
    print(total_entries)
    return(namelist)

getName()