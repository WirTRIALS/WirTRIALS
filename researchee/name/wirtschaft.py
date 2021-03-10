from ldap3 import Server, Connection, SUBTREE, LEVEL

def getNameFromWirtschaft():
    total_entries = 0
    connection_kwargs = {
        'server': 'ldap.tu-chemnitz.de',
        'auto_bind': True,
    }
    conn = Connection(**connection_kwargs)

        # paged search wrapped in a generator
    total_entries = 0
    entry_generator = conn.extend.standard.paged_search(search_base = 'ou=Users,dc=tu-chemnitz,dc=de',
            search_filter= '(& (objectClass=Person) (|(ou=*wirtschaft*)))',
                                                    search_scope = SUBTREE,
                                                    attributes = ['cn', 'ou', 'title'],
                                                    paged_size= 200,
                                                    get_operational_attributes=True)  
    namelist = []

    for entry in entry_generator:
        total_entries += 1
        name = ''.join(entry['attributes']['cn'])
        faculty = "Economics"
        professorship = ''.join(entry['attributes']['ou'][0])
        professorship_ = professorship.split("|")[0]
        title = "Researcher"
        if ''.join(entry['attributes']['title']) == "Prof.":
            title = "Professor"
        #print(entry['attributes']['title'])
        nameAndFaculty = name + '&' + title + '&' + professorship_
        namelist.append(nameAndFaculty)
    print(namelist)
    print(total_entries)
    return(namelist)

getNameFromWirtschaft()