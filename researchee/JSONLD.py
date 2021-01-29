# This module contains a procedure, which would create a file consisting of the name of a researcher from faculty of Computer Science and his/her expertise and professorship. The file is in the format of JSON-LD. In procedure, name.getName() and expertise.getExpertise() would be used.


from name import getName
from expertise import getExpertise
from rdflib import Graph, Namespace, URIRef, Literal, plugin, RDF
import random
import time


g = Graph()
researchee = Namespace("https://www.researchgate.com/profile/")
schema = Namespace("http://schema.org/")
topic = Namespace("https://www.researchgate.com/topic/")
g.bind("researchee", researchee)
g.bind("schema", schema)
g.bind("rdf", RDF)
context = {
    "name": schema+"name",
    "jobTitle": schema+"jobTitle",
    "memberOf": schema+"memberOf",
    "knowsAbout": schema+"knowsAbout"
}


namelist = getName(1)  # 1 refers to faculty of Computer Science

print("namelist has been got")


for nameAndFaculty in namelist:
    name = nameAndFaculty.split('&')[0]
    professorship = nameAndFaculty.split('&')[1]
    faculty = nameAndFaculty.split('&')[2]
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
        p6 = URIRef("knowsAbout")
        o6 = Literal(exp.replace("_", " "))
        # create a triple for researcher's expertise

        g.add((s, p6, o6))


print("RDF graph has been built")

g.serialize(destination="database4.json", context=context, format="json-ld")