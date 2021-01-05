#This module provides a user interface, which receive a researcher's name, and print his/her expertise out. The interface is running forever, until user type the commnad "exit". In program, sparql is used to query the file "database.rdf"
#input: name of a researcher
#output: his/her expertise

import rdflib
import requests

g = rdflib.Graph()

g.parse("dummy.rdf")

qres = g.query(
    """SELECT DISTINCT ?name ?expertise
       WHERE {
         ?a researchee:Name ?name .
         ?a researchee:hasExpertise ?expertise .
       }""")
print("Name   |  expertise")
for row in qres:
    print("%s  |  %s" % row)

    #incomplete still working