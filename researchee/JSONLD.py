<<<<<<< HEAD
from name import getAllName
from expertise import getExpertise
from rdflib import Graph,Namespace,URIRef,Literal,plugin,RDF
import random, time
import requests

g = Graph()
#g.parse("database2.json",format="json-ld")
researchee = Namespace("http://wirtrials.app.web/researchee#")
researchgate = Namespace("https://www.researchgate.net/profile/")
topic = Namespace("https://www.researchgate.net/topic/")
=======
# This module contains a procedure, which would create a file consisting of the name of a researcher from faculty of Computer Science and his/her expertise and professorship. The file is in the format of JSON-LD. In procedure, name.getName() and expertise.getExpertise() would be used.


from name import getName
from expertise import getExpertise
from rdflib import Graph, Namespace, URIRef, Literal, plugin, RDF
import random
import time


g = Graph()
researchee = Namespace("https://www.researchgate.com/profile/")
>>>>>>> ecde586b764238ed739ea80dca69bc80dd5c78f9
schema = Namespace("http://schema.org/")
topic = Namespace("https://www.researchgate.com/topic/")
g.bind("researchee", researchee)
g.bind("schema", schema)
g.bind("rdf", RDF)
<<<<<<< HEAD
g.bind("researchgate", researchgate)
g.bind("topic", topic)

namelist = getAllName()       #1 refers to faculty of Computer Science
=======
context = {
    "name": schema+"name",
    "jobTitle": schema+"jobTitle",
    "memberOf": schema+"memberOf",
    "knowsAbout": schema+"knowsAbout"
}


namelist = getName(1)  # 1 refers to faculty of Computer Science
>>>>>>> ecde586b764238ed739ea80dca69bc80dd5c78f9

print("namelist has been got")


for nameAndFaculty in namelist:
    name = nameAndFaculty.split('&')[0]
    name_ = '_'.join(name.split(' '))
    professorship = nameAndFaculty.split('&')[1]
    professorship_ = '_'.join(professorship.split(' '))
    faculty = nameAndFaculty.split('&')[2]
<<<<<<< HEAD
    faculty_ = '_'.join(faculty.split(' '))
    if name == 'Matthias Werner':
        name_ = 'Matthias-Werner'
    
    delay = 10 * random.random() + 5
    time.sleep(delay)
    try:
        r = requests.get("https://www.researchgate.net/profile/"+name_)
        s = URIRef(researchgate+name_)

    except:
        s = URIRef(researchee+name_)
    p = URIRef("name")
    o = Literal(name)
    g.add((s,p,o))              #create a triple for researcher's name
    
    p2 = URIRef("jobTitle")
    o2 = URIRef(researchee+"Professor")
    g.add((s,p2,o2))            #create a triple for researcher's position
    
    
    s3 = URIRef(researchee+professorship_)
    p3 = URIRef("name")
    o3 = Literal(professorship)
    g.add((s3,p3,o3))         #create a triple for professorship's name
    
    p7 = URIRef("type")
    o7 = URIRef(researchee+"Professorship")
    g.add((s3,p7,o7))            #create a triple for professorship's type
    
    p4 = URIRef("memberOf")
    g.add((s,p4,s3))          #create a triple for researcher's professorship
    
 
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
        
=======
#    print(professorship)
    s = URIRef(researchee+name)
    p = URIRef(schema+"name")
    o = Literal(name.replace("_", " "))
    g.add((s, p, o))  # create a triple for researcher's name

    p2 = URIRef(schema+"jobTitle")
    o2 = Literal("Professor")
    g.add((s, p2, o2))  # create a triple for researcher's position

    s3 = URIRef(researchee+professorship)
    p3 = URIRef(schema+"memberOf")
    o3 = Literal(professorship.replace("_", " "))
    g.add((s, p3, o3))  # create a triple for professorship's name

    expList = getExpertise(name)
    for exp in expList:
        #        print("    " + exp)
        s6 = URIRef(topic+"knowsAbout/"+name)
>>>>>>> ecde586b764238ed739ea80dca69bc80dd5c78f9
        p6 = URIRef("knowsAbout")
        o6 = Literal(exp.replace("_", " "))
        # create a triple for researcher's expertise

        g.add((s, p6, o6))


print("RDF graph has been built")

g.serialize(destination="database4.json", context=context, format="json-ld")