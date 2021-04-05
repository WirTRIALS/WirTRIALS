
from rdflib import Graph,Namespace

g = Graph()
#g.parse("demo_database.rdf")
g.parse("database.json",format="json-ld")

roles = Namespace("https://vocab.org/aiiso-roles/schema#")
aiiso = Namespace("https://vocab.org/aiiso/schema#")
example = Namespace("https://example.org/people/")
schema = Namespace("http://schema.org/")

g.bind("roles", roles)
g.bind("aiiso", aiiso)
g.bind("example", example)
g.bind("schema", schema)

greeting = '''************************************************************
*                                                          *
*              Welcome to use Researchee                   *
*                                                          *
************************************************************''';
print(greeting)
    
while 1:
  

    instruction = '''Instructions:
Enter '0', to get all researchers in our system;
Enter '1', to get all professorships of faculty Computer Science;
Enter '2', to get all expertises;
Enter '3' and researcher's name, to get all his/her expertises;
Enter '4' and researcher's name, to get his/her professorship;
Enter '5' and professorship's name, to get all researchers in it;
Enter '6' and expertise's name, to get all researchers who knows it;
Enter '7' and researcher's name, to get all colleagues in the same professorship;
Enter 'exit', to leave the system.
example: 3 Martin Gaedke
Please enter your instruction:'''

    print(instruction)
    ins = input()

    if ins == 'exit':
        break
    elif ins == '0':
        title = "researchee:Professor"
        queryStr = f"""SELECT DISTINCT ?professorname 
            WHERE {{ 
                ?a schema:jobTitle {title} .
                ?a schema:name ?professorname
                }}"""
        qres = g.query(queryStr)
        
        description = "Researcher List: "

        
    elif ins == '1':
        pro = "roles:Professor"
        queryStr = f"""SELECT DISTINCT ?professorship_name 
            WHERE {{ 
                ?a schema:jobTitle {pro} .
                ?a schema:name ?professorship_name 
                }}"""
        qres = g.query(queryStr)
        description = "Professorship List: "        

    elif ins == '2':
        exp = "researchee:Expertise"
        queryStr = f"""SELECT DISTINCT ?expertise_name 
            WHERE {{ 
                
                ?a rdf:type {exp} . 
                ?a schema:name ?expertise_name
                }}"""
        qres = g.query(queryStr)
        
        description = "Expertise List: "
        
    elif ins.startswith('3'):
        index = ins.index(' ')
        researcher_name = ins[index+1:]
        queryStr = f"""SELECT DISTINCT ?expertise_name 
            WHERE {{ 
                ?a schema:name "{researcher_name}" . 
                ?a schema:knowsAbout ?b . 
                ?b schema:name ?expertise_name . 
                }}"""
        qres = g.query(queryStr)

        description = "Expertises of %s: " %researcher_name

        
    elif ins.startswith('4'):
        index = ins.index(' ')
        researcher_name = ins[index+1:]
        queryStr = f"""SELECT DISTINCT ?professorship_name 
            WHERE {{ 
                ?a schema:name "{researcher_name}" .
                ?a schema:memberOf ?b . 
                ?b schema:name ?professorship_name .
                }}"""
        qres = g.query(queryStr)

        description = "Professorship of %s: " %researcher_name
    
    elif ins.startswith('5'):
        index = ins.index(' ')
        professorship_name = ins[index+1:]
        queryStr = f"""SELECT DISTINCT ?professor_name 
            WHERE {{ 
                ?a schema:name "{professorship_name}" .
                ?b schema:memberOf ?a . 
                ?b schema:name ?professor_name .
                }}"""
        qres = g.query(queryStr)

        description = "Researchers of %s: " %professorship_name    
    

    
    elif ins.startswith('6'):
        index = ins.index(' ')
        expertise_name = ins[index+1:]
        queryStr = f"""SELECT DISTINCT ?researcher_name 
            WHERE {{ 
                ?a schema:name "{expertise_name}" . 
                ?b schema:knowsAbout ?a . 
                ?b schema:name ?researcher_name . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Researchers who knows %s" %expertise_name 
    
    elif ins.startswith('7'):
        index = ins.index(' ')
        researcher_name = ins[index+1:]
        queryStr = f"""SELECT DISTINCT ?name 
            WHERE {{ 
                ?a schema:name "{researcher_name}" .
                ?a schema:memberOf ?b . 
                ?c schema:memberOf ?b . 
                ?c schema:name ?name . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Researchers in the same faculty with %s" %researcher_name 
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    print(description)
    if not qres:
        print("No information available")
    else:
        for row in qres:
            print("  %s" % row)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
