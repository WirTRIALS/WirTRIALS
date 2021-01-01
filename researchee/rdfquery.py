#getting name from RDF using sparql
import rdflib
import  requests
g = rdflib.Graph()

g.parse("dummy.rdf")

qres = g.query(
    """SELECT DISTINCT ?name ?expertise
       WHERE {
         ?a researchee:name ?name .
         ?a researchee:hasExpertise ?expertise .
       }""")
print("Name   |  expertise")
for row in qres:
    print("%s  |  %s" % row)

    #incomplete still working