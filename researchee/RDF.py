#This module contains a procedure, which would create a file consisting of the researcher's name and his/her expertise. The file is in the format of RDF. In procedure, name.getName() and expertise.getExpertise() would be used.


from rdflib import Graph,Namespace,URIRef,Literal,RDF,FOAF
from bs4 import BeautifulSoup
from requests import get
import random, time
import xml.etree.ElementTree as ET
import json

def mapExpertise(expertise):
    r = get("Http://experimental.worldcat.org/fast/search?query=oclc.topic+all+%22" + expertise +  "%22&sortKeys=usage&maximumRecords=1&httpAccept=application/xml")
    
    myroot = ET.fromstring(r.text)
    try:
        mytext = myroot.find('.//{http://www.loc.gov/MARC21/slim}subfield').text
        mytext = "http://experimental.worldcat.org/fast/" + mytext[3:]
    except:
        return ''


    return mytext

def mapToWikidata(expertise):

    API_ENDPOINT = "https://www.wikidata.org/w/api.php"

    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': expertise
    }

    r = get(API_ENDPOINT, params = params)

    print(r.json()['search'][0])
    
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



def addName():

    input = open("name_list.json", "r", encoding='utf8') 
    json_object = input.read()
    name_list = json.loads(json_object)

    g = Graph()
    #g.parse("database2.rdf")

    roles = Namespace("https://vocab.org/aiiso-roles/schema#")
    aiiso = Namespace("https://vocab.org/aiiso/schema#")
    example = Namespace("https://example.org/people/")
    
    g.bind("roles", roles)
    g.bind("aiiso", aiiso)
    g.bind("example", example)
    g.bind("foaf", FOAF)
    
    for nameAndTitle in name_list:

        #time.sleep(0.1)
        
        print("***********************************")
        print("***********************************")
        name = nameAndTitle.split('&')[0]
        title = nameAndTitle.split('&')[1]
        faculty_list = nameAndTitle.split('&')[2].split(' | ')
        
        faculty = faculty_list[len(faculty_list)-1]
        institute = ''
        professorship = ''
        
        if len(faculty_list)>1:
            professorship = faculty_list[0]
        if len(faculty_list)>2:
            institute = faculty_list[len(faculty_list)-2]


            
        # print(faculty)
        # print(institute)
        # print(professorship)
        
        nameID = mapName(name)
        if nameID == '':
            nameID = example + '+'.join(name.split(' '))
        print(nameID)
        
        s = URIRef(nameID)
        g.add((s,URIRef(FOAF.name),Literal(name)))
        g.add((s,URIRef(RDF.type),URIRef(roles + title)))
        g.add((s,URIRef(aiiso + "ResearchGroup"),Literal(professorship)))
        g.add((s,URIRef(aiiso + "Institute"),Literal(institute)))
        g.add((s,URIRef(aiiso + "Faculty"),Literal(faculty)))

    
    print("RDF graph has been built")

    g.serialize(destination="database2.rdf", format="xml")
    #g.serialize(destination="demo_database.rdf", format="xml")
    
    input.close()


def addExpertise():
    g = Graph()
    g.parse("database.rdf")

    schema = Namespace("http://schema.org/")
    g.bind("schema", schema)
    
    for s, p, o in g.triples((None, RDF.type, schema.Person)):
    
        if g.value(s,schema.traversed) == Literal('Yes'):
            #print("Yes")
            continue

        print("***********************************")
        print("***********************************")
        name = g.value(s,schema.name)
        print(name)


        expList = getExpertise(name)

        if len(expList) != 0:
            if expList[0] == "stop":
                print("validate browser")
                break
            for exp in expList:
                expID = mapExpertise(exp)
                
                if expID == '':
                    continue
                
                g.add((URIRef(expID),URIRef(schema + "name"),Literal(exp)))
                g.add((s,URIRef(schema + "knowsAbout"),URIRef(expID)))    
        
        g.remove((s,schema.traversed,None))
        g.add((s,URIRef(schema + "traversed"),Literal("Yes")))
        
        
            
    g.serialize(destination="database.rdf", format="xml")
    return


   
def mark():
    g = Graph()
    g.parse("database.rdf")

    schema = Namespace("http://schema.org/")
    g.bind("schema", schema)
    
    for s, p, o in g.triples((None, RDF.type, schema.Person)):
        g.add((s,URIRef(schema + "traversed"),Literal("No")))
    g.serialize(destination="database.rdf", format="xml")


def erase():
    g = Graph()
    g.parse("database.rdf")
    g.serialize(destination="database.rdf", format="xml")
    
#print(mapName("André Langer"))
#mapName("Matthias Werner")
#mapName("Dang Vu Nguyen Hai")  
#addExpertise()
#mark()
#addName()
#erase()
#print(mapExpertise("Human-Computer Interaction"))
#mapToWikidata('Image processing')