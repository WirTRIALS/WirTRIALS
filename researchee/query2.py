#getting name from RDF using sparql
import rdflib


g = rdflib.Graph()
g.parse("database3.rdf")
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
        queryStr = f"""SELECT DISTINCT ?age 
            WHERE {{ 
                ?a rdf:type ?b . 
                ?b ns1:age ?age . 
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

