""" 20-1 -- Web Scraper.

Modify your scraper to save the headlines in a file.
"""


import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        """ Scraper Initializer Method.
        
        Args:
            site: Site to scrape.
            
        Returns:
            None.
        """
        self.site = site


    def scrape(self):
        """ Scrape Web Page.
        
        Scrape web page and store results in results.txt.

        Args:
            None.

        Returns:
            None.
        """
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        parsed_output = BeautifulSoup(html, parser)

        with open("results.txt", "w") as file:
            for tag in parsed_output.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if "/news/" in url:
                    file.write("https://archlinux.org" + url + "\n")


news = "https://archlinux.org/news/"

Scraper(news).scrape()
