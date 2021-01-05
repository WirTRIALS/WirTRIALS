#This module contains a function, which could get all the expertises of a researher.
#Function Name: getExpertise()
#Parameters: a string which contains researcher's name
#Return Value: a list containing all the expertises of the researcher


from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# Scraping link
page_url = "https://link.springer.com/search?facet-creator=%22Martin+Gaedke%22"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds title from the springerlink page
containers = page_soup.find("a", {"class": "title"}).text
# print(containers)

expertise= page_soup.find("a",{"class":"facet-title"})
print(expertise)



# # Saving to local disk
# out_filename = "researchinfo.csv"
# # header of csv file to be written
# headers = "title, author_name \n"

# # opens file, and writes headers
# f = open(out_filename, "w")
# f.write(headers)

# # loops over each journals and grabs attributes about
# # each journal
# for container in containers:
#     # Finds all link tags "a" from within the first div.
#     make_rating_sp = container.title("a")
#     print(make_rating_sp)

#     co_author = make_rating_sp[0].img["title"].title()

#     author_name = container.div.select("a")[2].text

#     # Grabs the author information by searching
#     author_info = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "")

#     # prints the dataset to console
#     print("author: " + author + "\n")
#     print("co_author: " + co_author + "\n")
#     print("author_info: " + author_info + "\n")

#     # writes the dataset to file
#     f.write(brand + ", " + product_name.replace(",", "|") + ", " ")

# f.close()  # Close the file


# source = requests.get("https://link.springer.com/search?facet-creator=%22Martin+Gaedke%22").text
# soup = BeautifulSoup(source, 'lxml')

# expertise = soup.find("results-list")
# print(expertise)

    # return list()
    
# def getExpertiseTest(name):

#     expList = ["Software-Engineering","Web-Engineering"]
#     return expList
