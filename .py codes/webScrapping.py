import requests
from bs4 import BeautifulSoup
import os

# clear the screen
# os.system('cls')

url = "https://www.codewithharry.com/"

# get the content
r = requests.get(url)
htmlCont = r.content

# parse the content
soup = BeautifulSoup(htmlCont, 'html.parser')
soupCont = soup.prettify()

# content tree traversal
# print(soup.a.string)
anchors = soup.find_all('img')
all_links = set()

for link in anchors:
  if(link.get('src') != '#'):
    # linkTxt  = "https://www.codewithharry.com" + link.get('src')
    linkTxt = link.get('src')
    all_links.add(linkTxt)
    print(linkTxt)
exit()