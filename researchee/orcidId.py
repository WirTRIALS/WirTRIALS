import requests
import json

def getOrcidId(givenName,familyName):
    headers  = {"Accept": "application/json"}

    #parameters= given-names, family-name
    #searching with the parameters and adding boolean operators to get the best result
    api  = "https://pub.orcid.org/v3.0/search/?q=given-names:"+givenName+"+AND+family-name:"+familyName+"+AND+(('TU+Chemnitz'+OR+'Technical+University+of+Chemnitz'+OR+'Technische+Universität+Chemnitz')+OR+email:*tu-chemnitz*)"
    
    resp = requests.get(api,headers=headers)
    
    try:
        parsejson = resp.json()["result"][0]["orcid-identifier"]
        return parsejson["uri"]
    except:
        parsejson = ""  #returns empty result if no orcidid found
        return parsejson
    
   

