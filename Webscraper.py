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
        website_url = requests.get("https://myanimelist.net/topanime.php").text
        soup = BeautifulSoup(website_url, "lxml")  
        #print(soup)
        
        My_table = soup.find('table', {'class':'top-ranking-table'})
        new = My_table.findAll('img')
        for i in new:
            i = str(i)
            i=i.replace('&amp;#039;', '\'')
            name = i[17: i.find("\"", 10, 100)]
            #print(name)
            self.names.append(name)
             
    def scrapeRating(self):
        website_url = requests.get("https://myanimelist.net/topanime.php").text
        soup = BeautifulSoup(website_url, "lxml")  
        #print(soup)
        
        My_table = soup.find('table', {'class':'top-ranking-table'})
        new = My_table.findAll('span')
        for i in new:
            i = str(i)
            if (len(i)==53):
                #print(i)
                rating = i[42:46]
                self.ratings.append(rating)
                #print(rating)
            #print()
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