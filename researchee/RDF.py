#This module contains a procedure, which would create a file consisting of the researcher's name and his/her expertise. The file is in the format of RDF. In procedure, name.getAllName() and expertise.getExpertise() would be used.


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


from name import getAllName
from expertise import getExpertise
from rdflib import Graph,Namespace,URIRef,Literal
import random, time
import xml.etree.ElementTree as ET

def mapping(expertise):
    r = requests.get("Http://experimental.worldcat.org/fast/search?query=oclc.topic+all+%22" + expertise +  "%22&sortKeys=usage&maximumRecords=1&httpAccept=application/xml")
    
    myroot = ET.fromstring(r.text)
    try:
        mytext = myroot.find('.//{http://www.loc.gov/MARC21/slim}subfield').text
    except:
        mytext = ''
    #r = requests.get("http://id.worldcat.org/fast/" + mytext[3:] + "/rdf.xml")
    #check if the id is sensible

    #print(r.text)
    print(mytext)
    return mytext
#mapping("Embedded_Systems")


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
