<<<<<<< HEAD
#This module contains a procedure, which would create a file consisting of the researcher's name and his/her expertise. The file is in the format of RDF. In procedure, name.getAllName() and expertise.getExpertise() would be used.
=======
#This module contains a function, which could make a file consisting researcher's name and his/her expertise. The file is in the format of RDF. In function, name.getName() and expertise.getExpertise() would be used.
#Function Name: makeRDF()
#Parameters: empty
#Return Value: empty
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df

#RDF file for researchers name
#<rdf:RDF
# xmlns:researchee="http://wirtrials.app.web/researchee#"
# xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#researcher1">
#   <researchee:name>Martin Gaedke</researchee:name>
#   <researchee:hasExpertise rdf:resource="http://wirtrials.app.web/researchee#expertise1"/>
#   <researchee:hasExpertise rdf:resource="http://wirtrials.app.web/researchee#expertise3"/>  
# </rdf:Description>
#</rdf:RDF>

#RDF file for expertise
#<rdf:RDF
# xmlns:researchee="http://wirtrials.app.web/researchee#"
# xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#expertise1">
#   <researchee:name>Web engineering</researchee:name>
# </rdf:Description>
#</rdf:RDF>


<<<<<<< HEAD
from name import getAllName
from expertise import getExpertise
=======
from name import getName
from expertise import getExpertise,getExpertiseTest
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df
from rdflib import Graph,Namespace,URIRef,Literal
import random, time


<<<<<<< HEAD
g = Graph()
n = Namespace("http://wirtrials.app.web/researchee#")
g.bind("researchee", n)
namelist = getAllName()

print("namelist has been got")

s = URIRef(n+"Economic_and_Business_Administration")
p = URIRef(n+"facultyName")
o = Literal("Economic_and Business_Administration")
g.add((s,p,o))         #create a triple for faculty's name
for nameAndFaculty in namelist:
    name = nameAndFaculty.split('&')[0]
    faculty = nameAndFaculty.split('&')[1]
    s = URIRef(n+name)
    p = URIRef(n+"researcherName")
    o = Literal(name)
    g.add((s,p,o))            #create a triple for researcher's name
    
    s3 = URIRef(n+faculty)
    p4 = URIRef(n+"facultyName")
    o3 = Literal(faculty)
    g.add((s3,p4,o3))         #create a triple for faculty's name
    
    p4 = URIRef(n+"belongsTo")
    g.add((s,p4,s3))          #create a triple for researcher's faculty
    
 
#    expList = getExpertiseDemo(name)
    delay = 10 * random.random() + 10
    time.sleep(delay)
    print("after " + str(delay) + " seconds, now extracting " + name)
    
    expList = getExpertise(name)
    
    for exp in expList:
        s2 = URIRef(n+exp)
        p2 = URIRef(n+"expertiseName")
        o2 = Literal(exp)
        g.add((s2,p2,o2))   #create a triple for expertise's name
        
        p3 = URIRef(n+"hasExpertise")
        g.add((s,p3,s2))    #create a triple for researcher's expertise

print("RDF graph has been built")

g.serialize(destination="database.rdf", format="xml")
#g.serialize(destination="demo_database.rdf", format="xml")
print("RDF graph has been written into database.rdf")
=======
def makeRDF():

    g = Graph()
    n = Namespace("http://wirtrials.app.web/researchee#")
    g.bind("researchee", n)
    namelist = getName()
    for name in namelist:
        s = URIRef(n+name)
        p = URIRef(n+"name")
        o = Literal(name)
        g.add((s,p,o))          #create a triple for researcher's name
        expList = getExpertiseTest(name)
#        expList = getExpertise(name)
        for exp in expList:
            s2 = URIRef(n+exp)
            o2 = Literal(exp)
            g.add((s2,p,o2))    #create a triple for expertise's name
            p2 = URIRef(n+"hasExpertise")
            g.add((s,p2,s2))    #create a triple for researcher's expertise
        break;
    g.serialize(destination="database.rdf", format="xml")
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df
