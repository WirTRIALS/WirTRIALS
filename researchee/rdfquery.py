
import rdflib
import requests

g = rdflib.Graph()
g.parse("database.rdf")
n = 5
while n > 0:
    n -= 1

    print('\nEnter your desired name:')
    researchee_name = input()
    if researchee_name == "exit":
        break

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