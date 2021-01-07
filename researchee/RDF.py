#This module contains a procedure, which would create a file consisting of the researcher's name and his/her expertise. The file is in the format of RDF. In procedure, name.getName() and expertise.getExpertise() would be used.


#RDF file as database
#<rdf:RDF
# xmlns:researchee="http://wirtrials.app.web/researchee#"
# xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#Martin-Gaedke">
#   <researchee:researcherName>Martin-Gaedke</researchee:researcherName>
#   <researchee:hasExpertise rdf:resource="http://wirtrials.app.web/researchee#Web-Engineering"/>
#   <researchee:hasExpertise rdf:resource="http://wirtrials.app.web/researchee#Software-Engineering"/>  
# </rdf:Description>

# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#Web-Engineering">
#   <researchee:expertiseName>Web-Engineering</researchee:expertiseName>
# </rdf:Description>

# <rdf:Description rdf:about="http://wirtrials.app.web/researchee#Software-Engineering">
#   <researchee:expertiseName>Software-Engineering</researchee:expertiseName>
# </rdf:Description>

#</rdf:RDF>


from name import getName
from expertise import getExpertise
from rdflib import Graph,Namespace,URIRef,Literal


g = Graph()
n = Namespace("http://wirtrials.app.web/researchee#")
g.bind("researchee", n)
namelist = getName()
for name in namelist:
    s = URIRef(n+name)
    p = URIRef(n+"researcherName")
    o = Literal(name)
    g.add((s,p,o))          #create a triple for researcher's name
#    expList = getExpertiseTest(name)
    expList = getExpertise(name)
    for exp in expList:
        s2 = URIRef(n+exp)
        p2 = URIRef(n+"expertiseName")
        o2 = Literal(exp)
        g.add((s2,p2,o2))   #create a triple for expertise's name
        p3 = URIRef(n+"hasExpertise")
        g.add((s,p3,s2))    #create a triple for researcher's expertise
    
g.serialize(destination="database.rdf", format="xml")