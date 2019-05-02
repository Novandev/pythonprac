import requests
#import beautifulsoup parser
from bs4 import BeautifulSoup
#sets the url to be parsed
url = 'https://www.nytimes.com/'
#opens up and htps request to get the information abou the page
r = requests.get(url)
#parses the information in the page and sets it to a string
r_html = r.text
# turns it into a beautifulSoup object, so itll use the libraries
soup = BeautifulSoup(r_html)
# takes the a element as the parget to find all fo the href items and print

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
