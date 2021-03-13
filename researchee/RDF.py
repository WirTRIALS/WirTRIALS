#This module contains a procedure, which would create a file consisting of the researcher's name and his/her expertise. The file is in the format of RDF. In procedure, name.getName() and expertise.getExpertise() would be used.


from rdflib import Graph,Namespace,URIRef,Literal,RDF,FOAF,BNode
from bs4 import BeautifulSoup
from requests import get
import random, time
import json
from name import getName, mapName
from expertise import getExpertiseFromMicrosoft

#map expertise to FAST Linked Data
def mapExpertise(expertise):
    r = get("Http://experimental.worldcat.org/fast/search?query=oclc.topic+all+%22" + expertise +  "%22&sortKeys=usage&maximumRecords=1&httpAccept=application/xml")
    
    myroot = ET.fromstring(r.text)
    try:
        mytext = myroot.find('.//{http://www.loc.gov/MARC21/slim}subfield').text
        mytext = "http://experimental.worldcat.org/fast/" + mytext[3:]
    except:
        return ''


    return mytext

#map expertise to WikiData
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
    
def test():

    g = Graph()
    #g.parse("database2.rdf")

    
    s = URIRef('abc')
    o = BNode()
    g.add((o,URIRef('age'),Literal('30')))
    g.add((s,URIRef(RDF.type),o))
    g.add((s,URIRef(FOAF.name),Literal('ruge')))

    o2 = BNode()
    g.add((o2,URIRef(FOAF.age),Literal('24')))
    g.add((s,URIRef(RDF.type),o2))
    print("RDF graph has been built")

    str = g.serialize(format="json-ld")
    framed = jsonld.frame(str, frame)
    #g.serialize(destination="demo_database.rdf", format="xml")



def addName():
    input = open("name_list.json", "r", encoding='utf8') 
    json_object = input.read()
    name_list = json.loads(json_object)

    g = Graph()
    #g.parse("database.json")

    roles = Namespace("https://vocab.org/aiiso-roles/schema#")
    aiiso = Namespace("https://vocab.org/aiiso/schema#")
    example = Namespace("https://example.org/people/")
    schema = Namespace("http://schema.org/")
    
    g.bind("roles", roles)
    g.bind("aiiso", aiiso)
    g.bind("example", example)
    g.bind("schema", schema)
    
    count = 0
    for nameAndTitle in name_list:

        count += 1
        print(count)
        #time.sleep(0.1)
        
        #print("***********************************")
        #print("***********************************")
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
        g.add((s,URIRef(schema.name),Literal(name)))
        g.add((s,URIRef(RDF.type),URIRef(schema.Person)))
        g.add((s,URIRef(schema.jobTitle),URIRef(roles + title)))
        g.add((s,URIRef(aiiso + "ResearchGroup"),Literal(professorship)))
        g.add((s,URIRef(aiiso + "Institute"),Literal(institute)))
        g.add((s,URIRef(aiiso + "Faculty"),Literal(faculty)))

    
    print("RDF graph has been built")
    context = { "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "type": "rdf:type", "schema": "http://schema.org/", "roles": "https://vocab.org/aiiso-roles/schema#", "aiiso": "https://vocab.org/aiiso/schema#", "example": "https://example.org/people/" }
    g.serialize(destination="database.json", context = context, format="json-ld")
    #g.serialize(destination="demo_database.rdf", format="xml")
    
    input.close()


def addExpertise():
    g = Graph()
    g.parse("database.json",format="json-ld")
    schema = Namespace("http://schema.org/")
    
    for s, p, o in g.triples((None, RDF.type, schema.Person)):
        if g.value(s,schema.knowsAbout):
            print("visited")
            continue
            
        print("***********************************")
        print("***********************************")
        name = g.value(s,schema.name)
        print(name)

        dict = getExpertiseFromMicrosoft(name)
        #expList = dict['histograms'][0]['histogram']
        print(dict)
        if len(expList) != 0:

            for exp in expList:
                expID = mapToWikidata(exp)
                
                if expID == '':
                    continue
                
                g.add((URIRef(expID),URIRef(schema + "name"),Literal(exp)))
                g.add((s,URIRef(schema + "knowsAbout"),URIRef(expID)))    
        
        
        break
            
    #g.serialize(destination="database.rdf", format="xml")
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


#getName()
#addName()
#addExpertise()
#mark()

#erase()
#print(mapExpertise("Human-Computer Interaction"))
mapToWikidata('Image processing')