# Michael Wu (mvw5mf)

import urllib.request
import bs4
import re

web = urllib.request.urlopen("https://cs1110.cs.virginia.edu/souptest.html")
page = web.read()

parsedPage = bs4.BeautifulSoup(page, "html.parser")

for tag in parsedPage.find_all('h1'):
    print(tag)

web = urllib.request.urlopen("http://www.virginiasports.com/sports/m-baskbl/sched/va-m-baskbl-sched.html")
page = web.read()

parsedPage = bs4.BeautifulSoup(page, "html.parser")

for tag in parsedPage.find_all('td', class_="row-text"):
    print(tag)