#getting name from RDF using sparql
import rdflib
<<<<<<< HEAD

g = rdflib.Graph()
#g.parse("demo_database.rdf")
g.parse("database.rdf")
greeting = '''************************************************************
*                                                          *
*              Welcome to use Researchee                   *
*                                                          *
************************************************************''';
print(greeting)
    
while 1:
  

    instruction = '''Instructions:
Enter '0', to get all professors who have expertises in our system;
Enter '1', to get all faculties of TUC;
Enter '2', to get all expertises;
Enter '3' and professor's name, to get all his/her expertises;
Enter '4' and professor's name, to get his/her faculty;
Enter '5' and faculty's name, to get all professor of that faculty;
Enter '6' and expertise's name, to get all professors who owns it;
Enter '7' and professor's name, to get all professors in the same faculty;
Enter 'exit', to leave the system.
Please enter your instruction:'''

    print(instruction)
    ins = input()

    if ins == 'exit':
        break
    elif ins == '0':
        queryStr = f"""SELECT DISTINCT ?researcher_name 
            WHERE {{ 
                ?a researchee:researcherName ?researcher_name . 
                ?a researchee:hasExpertise ?expertise . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Professor List: "

        
    elif ins == '1':
        queryStr = f"""SELECT DISTINCT ?faculty_name 
            WHERE {{ 
                ?a researchee:facultyName ?faculty_name . 
                }}"""
        qres = g.query(queryStr)
        description = "Faculty List: "        

    elif ins == '2':
        queryStr = f"""SELECT DISTINCT ?expertise_name 
            WHERE {{ 
                ?a researchee:expertiseName ?expertise_name . 
                ?b researchee:hasExpertise ?a . 
                ?c researchee:hasExpertise ?a . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Expertise List: "
        
    elif ins.startswith('3'):
        researcher_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?exp 
            WHERE {{ 
                ?a researchee:researcherName "{researcher_name}" . 
                ?a researchee:hasExpertise ?expertise . 
                ?expertise researchee:expertiseName ?exp . 
                }}"""
        qres = g.query(queryStr)

        description = "Expertises of %s: " %researcher_name

        
    elif ins.startswith('4'):
        researcher_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?faculty_name 
            WHERE {{ 
                ?a researchee:researcherName "{researcher_name}" .
                ?a researchee:belongsTo ?b . 
                ?b researchee:facultyName ?faculty_name .
                }}"""
        qres = g.query(queryStr)

        description = "Faculty of %s: " %researcher_name
    
    elif ins.startswith('5'):
        faculty_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?researcher_name 
            WHERE {{ 
                ?a researchee:facultyName "{faculty_name}" .
                ?b researchee:belongsTo ?a . 
                ?b researchee:researcherName ?researcher_name .
                }}"""
        qres = g.query(queryStr)

        description = "Professors of %s: " %faculty_name    
    

    
    elif ins.startswith('6'):
        expertise_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?researcher_name 
            WHERE {{ 
                ?a researchee:expertiseName "{expertise_name}" . 
                ?b researchee:hasExpertise ?a . 
                ?b researchee:researcherName ?researcher_name . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Researchers who has expertise %s" %expertise_name 
    
    elif ins.startswith('7'):
        researcher_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?name 
            WHERE {{ 
                ?a researchee:researcherName "{researcher_name}" .
                ?a researchee:belongsTo ?b . 
                ?c researchee:belongsTo ?b . 
                ?c researchee:researcherName ?name . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Professors in the same faculty with %s" %researcher_name 
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(description)
    if not qres:
        print("No information available")
    else:
        for row in qres:
            print("  %s" % row)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
=======
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
>>>>>>> a3df2674926963986d71fdb71b145879aadaa8df
