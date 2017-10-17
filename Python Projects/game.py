# Michael Wu (mvw5mf)

import urllib.request, bs4, random

def get_links(url):
    web = urllib.request.urlopen(url)
    page = web.read()

    parsedPage = bs4.BeautifulSoup(page, "html.parser")
    links = []

    for tag in parsedPage.find_all('a', {"href" : True}):
        if tag['href'].startswith('/wiki/'):
            links.append(tag['href'])
    return links

def pick_random_link(list_of_links):
    rand_int = random.randint(0,len(list_of_links)-1)

    while list_of_links[rand_int].find("File:") != -1:
        rand_int = random.randint(0,len(list_of_links)-1)

    return list_of_links[rand_int]

print("Welcome to the Wikipedia Game!")
url = input("What page do you want to start with?: ")
hops = int(input("What is the maximum number of hops?: "))
url = 'https://en.wikipedia.org/wiki/' + url
url = url.replace(' ', '_')
path = []
path.append(url)
while hops > 0:
    link_list = get_links(url)
    url = 'https://en.wikipedia.org' + pick_random_link(link_list)
    path.append(url)
    hops -= 1

print("Game created!")
print("You need to get from:", path[0])
print("To:", path[-1])
input("Press Enter to see the answer!")

for link in path:
    print(link)