import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv
new_list = ["https://www.nytimes.com/", "https://www.bbc.com/news",
            "https://timesofindia.indiatimes.com/"]
total_urls = []


def fetchArticles():
    for i in new_list:
        url = i
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))
        if(url == "https://www.nytimes.com/"):
            for i in urls:
                for j in i.split():
                    if j.startswith("https://www."):
                        total_urls.append(j)
            with open('innovators.csv', 'a') as file:
                for i in total_urls:
                    file.write(i)
                    file.write('\n')
        if(url == "https://www.bbc.com/news"):
            for i in urls:
                for j in i.split():
                    if j.startswith("/n"):
                        total_urls.append("https://www.bbc.com"+j)
            with open('innovators.csv', 'a') as file:
                for i in total_urls:
                    file.write(i)
                    file.write('\n')
    

    remove_duplicates = list(set(total_urls))
    pprint(remove_duplicates)
    return remove_duplicates
