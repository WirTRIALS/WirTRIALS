#This module contains a function, which could make a file consisting researcher's name and his/her expertise. The file is in the format of RDF. In function, name.getName() and expertise.getExpertise() would be used.
#Function Name: makeRDF()
#Parameters: empty
#Return Value: empty

#RDF file for researchers name
#<rdf:RDF
# xmlns:researchee="http://wirtrials.app.web/researchee#"
# xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#researcher1">
#   <researchee:researcherName>Martin Gaedke</researchee:name>
#   <researchee:hasExpertise rdf:resource="http://wirtrials.app.web/researchee#Web-Engineering"/>
#   <researchee:hasExpertise rdf:resource="http://wirtrials.app.web/researchee#Software-Engineering"/>  
# </rdf:Description>

# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#Web-Engineering">
#   <researchee:expertiseName>Web Engineering</researchee:name>
# </rdf:Description>
# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#Software-Engineering">
#   <researchee:expertiseName>Software Engineering</researchee:name>
# </rdf:Description>
#</rdf:RDF>


from name import getName
from expertise import getExpertiseTest
from rdflib import Graph,Namespace,URIRef,Literal

def makeRDF():

    g = Graph()
    n = Namespace("http://wirtrials.app.web/researchee#")
    g.bind("researchee", n)
    namelist = getName()
    for name in namelist:
        s = URIRef(n+name)
        p = URIRef(n+"researcherName")
        o = Literal(name)
        g.add((s,p,o))          #create a triple for researcher's name
        expList = getExpertiseTest(name)
#        expList = getExpertise(name)
        for exp in expList:
            s2 = URIRef(n+exp)
            p2 = URIRef(n+"expertiseName")
            o2 = Literal(exp)
            g.add((s2,p2,o2))    #create a triple for expertise's name
            p3 = URIRef(n+"hasExpertise")
            g.add((s,p3,s2))    #create a triple for researcher's expertise
        break;
    g.serialize(destination="database.rdf", format="xml")

makeRDF()