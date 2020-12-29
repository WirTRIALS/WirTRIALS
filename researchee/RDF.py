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


import name
import expertise
def makeRDF():


