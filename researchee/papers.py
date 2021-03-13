#This module contains a function, which could get all the papers of a researher and store them into a json file.
#Function Name: getPapers()
#Input: name_list.json
#Output: paper_dict.json

from requests import get
import random, time
import json

#get all papers of all names and store them into a json file, including information of years, coauthors, title, DOI, cites
def getExpertise():