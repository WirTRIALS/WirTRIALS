from name import getAllName
from expertise import getExpertise
from rdflib import Graph,Namespace,URIRef,Literal,plugin,RDF
import random, time
import requests

g = Graph()
g.parse("database2.json",format="json-ld")
researchee = Namespace("http://wirtrials.app.web/researchee#")
researchgate = Namespace("https://www.researchgate.net/profile/")
topic = Namespace("https://www.researchgate.net/topic/")
schema = Namespace("http://schema.org/")
g.bind("researchee", researchee)
g.bind("schema", schema)
g.bind("rdf", RDF)
g.bind("researchgate", researchgate)
g.bind("topic", topic)

namelist = getAllName()       #1 refers to faculty of Computer Science

print("namelist has been got")


for nameAndFaculty in namelist:
    name = nameAndFaculty.split('&')[0]
    name_ = '_'.join(name.split(' '))
    professorship = nameAndFaculty.split('&')[1]
    professorship_ = '_'.join(professorship.split(' '))
    faculty = nameAndFaculty.split('&')[2]
    faculty_ = '_'.join(faculty.split(' '))

    
    delay = 2 * random.random() + 2
    time.sleep(delay)
    try:
        r = requests.get("https://www.researchgate.net/profile/"+name_)
        s = URIRef(researchgate+name_)

    except:
        s = URIRef(researchee+name_)
 
 
    expList = getExpertise(name_)
    for exp_ in expList:
        exp = ' '.join(exp_.split('_'))

        s5 = URIRef(topic+exp_)
        p5 = URIRef("name")
        o5 = Literal(exp)
        g.add((s5,p5,o5))   #create a triple for expertise's name
        
        p8 = URIRef("type")
        o8 = URIRef(researchee+"Expertise")
        g.add((s5,p8,o8))   #create a triple for expertise's type
        
        p6 = URIRef("knowsAbout")
        g.add((s,p6,s5))    #create a triple for researcher's expertise


    
print("RDF graph has been built")
context = {"@vocab": schema , "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "type": "rdf:type" }
g.serialize(destination = "database2.json", context = context, format = "json-ld")
#g.serialize(destination="demo_database.rdf", format="xml")
print("RDF graph has been written into database2.json")