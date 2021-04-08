#getting name from RDF using sparql
import rdflib


g = rdflib.Graph()
#g.parse("demo_database.rdf")
g.parse("database2.rdf")
greeting = '''************************************************************
*                                                          *
*              Welcome to use Researchee                   *
*                                                          *
************************************************************''';
print(greeting)
    
while 1:
  

    instruction = '''Instructions:
Enter '0', to get all professors who have expertises in our system;
Enter '2', to get all expertises;
Enter '3' and professor's name, to get all his/her expertises;
Enter '6' and expertise's name, to get all professors who owns it;

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


    elif ins == '2':
        queryStr = f"""SELECT DISTINCT ?expertise_name 
            WHERE {{ 
                ?a researchee:expertiseName ?expertise_name . 
                ?b researchee:hasExpertise ?a . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Expertise List: "
        
    elif ins.startswith('3'):
        researcher_name = ' '.join(ins.split(' ')[1:])
        queryStr = f"""SELECT DISTINCT ?exp 
            WHERE {{ 
                ?a researchee:researcherName "{researcher_name}" . 
                ?a researchee:hasExpertise ?expertise . 
                ?expertise researchee:expertiseName ?exp . 
                }}"""
        qres = g.query(queryStr)

        description = "Expertises of %s: " %researcher_name

    elif ins.startswith('6'):
        expertise_name = ins.split(' ')[1
        queryStr = f"""SELECT DISTINCT ?researcher_name 
            WHERE {{ 
                ?a researchee:expertiseName "{expertise_name}" . 
                ?b researchee:hasExpertise ?a .
                ?b researchee:researcherName ?researcher_name .
                }}"""
        qres = g.query(queryStr)
        
        description = "Professor List: "

   

    else:
        description = "Invalid command"
        qres = ''
        
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(description)
    if not qres:
        print("No information available")
    else:
        for row in qres:
            print("  %s" % row)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

