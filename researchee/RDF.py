#This module contains a procedure, which would create a file consisting of the researcher's name and his/her expertise. The file is in the format of RDF. In procedure, name.getName() and expertise.getExpertise() would be used.



from name.name import getName
from expertise import getExpertise
from rdflib import Graph,Namespace,URIRef,Literal,RDF
import random, time
import xml.etree.ElementTree as ET
<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests

def mapExpertise(expertise):
=======

def mapping(expertise):
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
    r = requests.get("Http://experimental.worldcat.org/fast/search?query=oclc.topic+all+%22" + expertise +  "%22&sortKeys=usage&maximumRecords=1&httpAccept=application/xml")
    
    myroot = ET.fromstring(r.text)
    try:
        mytext = myroot.find('.//{http://www.loc.gov/MARC21/slim}subfield').text
<<<<<<< HEAD
        mytext = "http://experimental.worldcat.org/fast/" + mytext[3:]
    except:
        return ''

=======
    except:
        mytext = ''
    #r = requests.get("http://id.worldcat.org/fast/" + mytext[3:] + "/rdf.xml")
    #check if the id is sensible

    #print(r.text)
    print(mytext)
    return mytext
#mapping("Embedded_Systems")
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176

    return mytext

<<<<<<< HEAD

def mapName(name):
    firstName = name.split(' ')[0]
    lastName = " ".join(name.split(' ')[1:])
    r = requests.get("https://pub.orcid.org/v3.0/expanded-search/?q=(given-names%3A" + firstName + ")%20AND%20(family-name%3A" + lastName +")%20AND%20affiliation-org-name%3Achemnitz&start=0&rows=1")
    
    #print(r.text)
    
    myroot = ET.fromstring(r.text)
    try:
        mytext = myroot.find('.//{http://www.orcid.org/ns/expanded-search}orcid-id').text
    except:
        mytext = ''
=======
g = Graph()
schema = Namespace("http://schema.org/")
g.bind("schema", schema)
namelist = getName()

print("namelist has been got")

for nameAndFaculty in namelist:
    name = nameAndFaculty.split('&')[0]
    professorship = nameAndFaculty.split('&')[1]
    faculty = nameAndFaculty.split('&')[2]
    
    s = URIRef(n+name)
    p = URIRef(n+"researcherName")
    o = Literal(name)
    g.add((s,p,o))            #create a triple for researcher's name
>>>>>>> cdce3ce0d6f4428f6f7c048953144568b3c26176
    
    if mytext == '':
        r = requests.get("https://pub.orcid.org/v3.0/expanded-search/?q=(given-names%3A" + firstName + ")%20AND%20(family-name%3A" + lastName +")%20&start=0&rows=1")
        
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



def makeRDF():
    g = Graph()
    g.parse("database.rdf")

    schema = Namespace("http://schema.org/")
    g.bind("schema", schema)
    
    '''
    for s, p, o in g.triples((None, RDF.type, schema.Person)):
        if g.value(s,schema.knowsAbout):
            print("has")
            continue
        name = g.value(s,schema.name)
        print(name)
    return 
    '''
    
    namelist = getName()

    print("namelist has been got")

    for nameAndTitle in namelist:
        print("***********************************")
        print("***********************************")
        name = nameAndTitle.split('&')[0]
        title = nameAndTitle.split('&')[1]
        try:
            professorship = nameAndTitle.split('&')[2]
        except:
            professorship = ''
        
        nameID = mapName(name)
        
        print(name + " " + nameID)
        if nameID == '':
            continue
        
        
        g.add((URIRef(nameID),URIRef(schema + "name"),Literal(name)))
        g.add((URIRef(nameID),URIRef(RDF.type),URIRef(schema + "Person")))
        g.add((URIRef(nameID),URIRef(schema + "jobTitle"),Literal(title)))         
        g.add((URIRef(nameID),URIRef(schema + "memberOf"),Literal(professorship)))
        

    
    print("RDF graph has been built")

    g.serialize(destination="database.rdf", format="xml")
    #g.serialize(destination="demo_database.rdf", format="xml")
    print("RDF graph has been written into database.rdf")



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
    
#mapName("Martin Gaedke")
#mapName("Matthias Werner")
#mapName("Dang Vu Nguyen Hai")  
#addExpertise()
#mark()
#makeRDF()
#erase()
#print(mapExpertise("Human-Computer Interaction"))
