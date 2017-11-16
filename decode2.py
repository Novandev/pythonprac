import requests
#import beautifulsoup parser
from bs4 import BeautifulSoup
#sets the url to be parsed
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
#opens up and htps request to get the information abou the page
r = requests.get(url)
#parses the information in the page and sets it to a string
r_html = r.text
# turns it into a beautifulSoup object, so itll use the libraries
soup = BeautifulSoup(r_html)
# takes the a element as the parget to find all fo the href items and print
def makeParagraph():
    data = ""
    for paragraph in soup.find_all('p'):
        data += paragraph.text.replace("\n", " ").strip()

    return data

printable= makeParagraph()

print(printable)
