
import rdflib
from rdflib import Graph,Namespace

g = rdflib.Graph()
#g.parse("demo_database.rdf")
g.parse("database2.json",format="json-ld")

researchee = Namespace("http://wirtrials.app.web/researchee#")
schema = Namespace("http://schema.org/")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g.bind("researchee", researchee)
g.bind("schema", schema)


greeting = '''************************************************************
*                                                          *
*              Welcome to use Researchee                   *
*                                                          *
************************************************************''';
print(greeting)
    
while 1:
  

    instruction = '''Instructions:
Enter '0', to get all professors in our system;
Enter '1', to get all professorships of faculty Computer Science;
Enter '2', to get all expertises;
Enter '3' and professor's name, to get all his/her expertises;
Enter '4' and professor's name, to get his/her professorship;
Enter '5' and professorship's name, to get all professors in it;
Enter '6' and expertise's name, to get all professors who knows it;
Enter '7' and professor's name, to get all colleagues in the same professorship;
Enter 'exit', to leave the system.
space(' ') between name should be replaced by underscore('_')
example: 3 Martin_Gaedke
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
        
        description = "Professor List: "

        
    elif ins == '1':
        pro = "researchee:Professorship"
        queryStr = f"""SELECT DISTINCT ?professorship_name 
            WHERE {{ 
                ?a rdf:type {pro} .
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
        researcher_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?expertise_name 
            WHERE {{ 
                ?a schema:name "{researcher_name}" . 
                ?a schema:knowsAbout ?b . 
                ?b schema:name ?expertise_name . 
                }}"""
        qres = g.query(queryStr)

        description = "Expertises of %s: " %researcher_name

        
    elif ins.startswith('4'):
        researcher_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?professorship_name 
            WHERE {{ 
                ?a schema:name "{researcher_name}" .
                ?a schema:memberOf ?b . 
                ?b schema:name ?professorship_name .
                }}"""
        qres = g.query(queryStr)

        description = "Professorship of %s: " %researcher_name
    
    elif ins.startswith('5'):
        professorship_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?professorship_name 
            WHERE {{ 
                ?a schema:name "{professorship_name}" .
                ?b schema:memberOf ?a . 
                ?b schema:name ?professorship_name .
                }}"""
        qres = g.query(queryStr)

        description = "Professors of %s: " %professorship_name    
    

    
    elif ins.startswith('6'):
        expertise_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?researcher_name 
            WHERE {{ 
                ?a schema:name "{expertise_name}" . 
                ?b schema:knowsAbout ?a . 
                ?b schema:name ?researcher_name . 
                }}"""
        qres = g.query(queryStr)
        
        description = "Researchers who knows %s" %expertise_name 
    
    elif ins.startswith('7'):
        researcher_name = ins.split(' ')[1]
        queryStr = f"""SELECT DISTINCT ?name 
            WHERE {{ 
                ?a schema:name "{researcher_name}" .
                ?a schema:memberOf ?b . 
                ?c schema:memberOf ?b . 
                ?c schema:name ?name . 
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
