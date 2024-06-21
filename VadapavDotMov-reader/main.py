import os

from bs4 import BeautifulSoup
import requests


class Download:

    def __init__(self):
        site = input("please input the root folder of the show you want to download: ")
        self.find(site)

    def find(self, site):
        soup = self.siteinit(site)
        directory = self.entries(soup)
        directory.pop(0)
        if len(directory) == 0:
            files = soup.find_all("a", "file-entry")
            for x in files:
                file = x['href']
                name = x.text.strip()
                os.system('curl --output "' + name + '" https://vadapav.mov' + file)
        else:
            for x in directory:
                link = x['href']
                self.find("https://vadapav.mov" + link)

    @staticmethod
    def siteinit(webbedsite):  # Grabs the HTML of the website
        site = requests.get(webbedsite)
        soup: BeautifulSoup = BeautifulSoup(site.text, features="lxml")
        return soup

    @staticmethod
    def entries(soup) -> list:
        directory_entry = soup.find_all("a", "directory-entry")
        return directory_entry


Download()
