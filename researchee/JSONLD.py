#This module contains a procedure, which would create a file consisting of the name of a researcher from faculty of Computer Science and his/her expertise and professorship. The file is in the format of JSON-LD. In procedure, name.getName() and expertise.getExpertise() would be used.


from name import getName
from expertise import getExpertise
from rdflib import Graph,Namespace,URIRef,Literal,plugin,RDF
import random, time


g = Graph()
researchee = Namespace("http://wirtrials.app.web/researchee#")
schema = Namespace("http://schema.org/")
g.bind("researchee", researchee)
g.bind("schema", schema)
g.bind("rdf", RDF)

namelist = getName(1)       #1 refers to faculty of Computer Science

print("namelist has been got")


for nameAndFaculty in namelist:
    name = nameAndFaculty.split('&')[0]
    professorship = nameAndFaculty.split('&')[1]
    faculty = nameAndFaculty.split('&')[2]
#    print(professorship)
    s = URIRef(researchee+name)
    p = URIRef("name")
    o = Literal(name)
    g.add((s,p,o))              #create a triple for researcher's name
    
    p2 = URIRef("jobTitle")
    o2 = URIRef(researchee+"Professor")
    g.add((s,p2,o2))            #create a triple for researcher's position
    

    s3 = URIRef(researchee+professorship)
    p3 = URIRef("name")
    o3 = Literal(professorship)
    g.add((s3,p3,o3))         #create a triple for professorship's name
    
    p7 = URIRef("type")
    o7 = URIRef(researchee+"professorship")
    g.add((s3,p7,o7))            #create a triple for professorship's type
    
    p4 = URIRef("memberOf")
    g.add((s,p4,s3))          #create a triple for researcher's professorship
    
 
    expList = getExpertise(name)
    for exp in expList:
#        print("    " + exp)
        s5 = URIRef(researchee+exp)
        p5 = URIRef("name")
        o5 = Literal(exp)
        g.add((s5,p5,o5))   #create a triple for expertise's name
        
        p8 = URIRef("type")
        o8 = URIRef(researchee+"expertise")
        g.add((s5,p8,o8))   #create a triple for expertise's type
        
        p6 = URIRef("knowsAbout")
        g.add((s,p6,s5))    #create a triple for researcher's expertise

    
print("RDF graph has been built")
context = {"@vocab": schema, "type": "rdf:type" }
g.serialize(destination = "database2.json", context = context, format = "json-ld")
#g.serialize(destination="demo_database.rdf", format="xml")
print("RDF graph has been written into database2.json")