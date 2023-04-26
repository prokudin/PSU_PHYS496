import urllib.request, urllib.parse
import json
import ssl
import validators
#API Implementation 

# Ignores unnecesary SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def url_parser(url): # Returns data in json format 
  if not bool(validators.url(url)): raise ValueError(f'Bad URL: {url}') # URL format check

  html = urllib.request.urlopen(url, context = ctx) #Handle for URL inputted
  # soup = bs4.BeautifulSoup(html, 'html.parser')
  data = html.read().decode()

  try:
    json_data = json.loads(data)
  except Exception as e:
    json_data = None
    print(e)

  return json_data

#Will be done by wednsday
def url_construct(api_url: str, url_elements: dict, identifiers: list, search: bool): # Constructs URL to get search query or obtain record
  
  parameters = {}

  if search: 
    for key, value in url_elements.items():
      parameters[key] = value
    extension = '?' + urllib.parse.urlencode(parameters)
  else:
    extension = ''

  url = api_url + extension
  
  return url

api_url = 'https://inspirehep.net/api/'
internal_identifiers = ['literature', 'authors', 'institutions', 'conferences', 'seminars', 'journals', 'jobs', 'experiments', 'data']
external_identifiers = ['doi', 'arxiv', 'orcid']

# import re

# test = None
# # refactoring of code above
# citation_list = re.findall('\{(.+)*\,(.+)*\,(.+)*\}', test)
# citation_list

url_parser(url_construct({}))