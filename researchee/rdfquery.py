
import rdflib
import requests

g = rdflib.Graph()
g.parse("database.rdf")

print('Enter your desired name:')
researchee_name = input()

queryStr = f"""SELECT DISTINCT ?exp 
          WHERE {{ 
             ?a researchee:researcherName "{researchee_name}" . 
             ?a researchee:hasExpertise ?expertise . 
             ?expertise researchee:expertiseName ?exp . 
            }}"""
qres = g.query(queryStr)

print("Expertise of %s: " %researchee_name)
if not qres:
    print("No information available")
else:
    for row in qres:
         print(" %s" % row)