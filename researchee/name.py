#This module contains a function, which could get all the names of TU Chemnitz and store them into a json file.
#Function Name: getName()
#Input: empty
#Output: name_list.json

from ldap3 import Server, Connection, SUBTREE, LEVEL
from string import ascii_lowercase
from itertools import product
from requests import get
import xml.etree.ElementTree as ET
import time
import json

#get all names and store them into a json file
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
                attributes = ['cn','givenName', 'sn', 'ou', 'title','uid'],
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
            print(entry)
        if pause_counter == 2:
            delay = 0.1
            time.sleep(delay)
            pause_counter = 0
        
    json_object = json.dumps(namelist, ensure_ascii=False) 
    
    with open("name_list.json", "w", encoding='utf8') as outfile: 
        outfile.write(json_object)
    
    print(total_entries)
    print("name list has been written into name_list.json")

#map name to ORCiD
def mapName(name):
    firstName = name.split(' ')[0]
    lastName = " ".join(name.split(' ')[1:])
    r = get("https://pub.orcid.org/v3.0/expanded-search/?q=(given-names%3A" + firstName + ")%20AND%20(family-name%3A" + lastName +")%20AND%20affiliation-org-name%3Achemnitz&start=0&rows=1")
    
    #print(r.text)
    
    myroot = ET.fromstring(r.text)
    try:
        mytext = myroot.find('.//{http://www.orcid.org/ns/expanded-search}orcid-id').text
    except:
        mytext = ''
    
    if mytext == '':
        r = get("https://pub.orcid.org/v3.0/expanded-search/?q=(given-names%3A" + firstName + ")%20AND%20(family-name%3A" + lastName +")%20&start=0&rows=1")
        
        #print(r.text)
        
        myroot = ET.fromstring(r.text)
        try:
            mytext = myroot.find('.//{http://www.orcid.org/ns/expanded-search}orcid-id').text
        except:
            mytext = ''
    
    
    if mytext == '':
        return ''
    else:
        mytext = "https://orcid.org/" + mytext
        #print(mytext)
        return mytext

#just for test
def readName():
    input = open("name_list.json", "r", encoding='utf8') 
    json_object = input.read()
    name_list = json.loads(json_object)
    list2 = set()
    for name in name_list:
        name = name.split('&')[0].strip()
        if name in list2:
            print(name)
        list2.add(name)
    print(len(list2))
    input.close()
    
#readName()