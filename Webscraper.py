from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import csv

class WebScrape():
    def __init__(self):
        #print()
        self.names = []
        self.ratings = []
        self.dictionary = {}
    def scrapeName(self):
        for i in range(5):
            url = "https://myanimelist.net/topanime.php?limit="+str(i*50)
            website_url = requests.get(url).text
            soup = BeautifulSoup(website_url, "lxml")  
            #print(soup)
            
            My_table = soup.find('table', {'class':'top-ranking-table'})
            new = My_table.findAll('img')
            for i in new:
                i = str(i)
                i=i.replace('&amp;#039;', '\'')
                i=i.replace(' amp;quot;', '\"')
                name = i[17: i.find("\"", 10, 100)]
                #print(name)
                refinedName=""
                for char in name:
                    if (char=="u\u03a8" or char == "Ψ" or char=="u\u03bc" or char == "μ" or char =="Μ" or char=="u\u0394" or char == "Δ" or char =="δ" or char=="u\u03c7" or char == "Χ" or char =="χ"):
                        pass
                    elif (char.isalpha() or char.isdigit() or char=="!" or char=="-" or char==":" or char==";" or char==" " or char=="/" or char=="(" or char==")" or char=="\'"):
                        refinedName = refinedName + char
                if (refinedName.find("border0") != -1):
                    refinedName = refinedName[0:refinedName.find("border0")]
                self.names.append(refinedName)
              
        #print(self.names)  
    def scrapeRating(self):
        for k in range(5):
            url = "https://myanimelist.net/topanime.php?limit="+str(k*50)
            website_url = requests.get(url).text
            soup = BeautifulSoup(website_url, "lxml")  
            #print(soup)
            
            My_table = soup.find('table', {'class':'top-ranking-table'})
            new = My_table.findAll('span')
            for i in new:
                i = str(i)
                if (len(i)==53):
                    
                    rating = i[42:46]
                    self.ratings.append(rating)
                    
    def getDictionary(self):

        for i in range(len(self.names)):
            self.dictionary[self.names[i]]=self.ratings[i]
           
        datafile = open("NamesAndRatings.csv", "w")

        writer = csv.writer(datafile)
        for name, rating in self.dictionary.items():
            writer.writerow([name, rating])
        datafile.close()
        return self.dictionary
web = WebScrape()
web.scrapeRating()
web.scrapeName()
print(web.getDictionary())