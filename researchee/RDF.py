#This module contains a function, which could make a file consisting researcher's name and his/her expertise. The file is in the format of RDF. In function, name.getName() and expertise.getExpertise() would be used.
#Function Name: makeRDF()
#Parameters: empty
#Return Value: empty

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


from name import getName
from expertise import getExpertise,getExpertiseTest
from rdflib import Graph,Namespace,URIRef,Literal

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