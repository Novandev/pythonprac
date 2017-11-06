import requests
#sets the url to be parsed
url = 'https://www.nytimes.com/'
#opens up and htps request to get the information abou the page
r = requests.get(url)
#parses the information in the page and sets it to a string
r_html = r.text
