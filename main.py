# import re
# import random
def short_url(url:str, lenth:int):
  # Handeling Dependency Imports
  try:
    from re import sub
    from random import randint
  except ImportError:
    from re import sub
    from random import randint

  # Getting Domain from URL
  url_split = url.split('/')
  domain = ''.join([url_split[0],'//',url_split[2]])

  # Strping the URL with Regex
  url_striped = sub('[&#?/@:.=-]', '', url)
  # Adding some extra number at the End of Striped URL
  extra = str(randint(12345678,1234567890))
  main_url = url_striped+extra

  # Creating an Empty List to store the short url letters
  str_list = []

  # itterating over the length of range and adding indivisual letters to the str_list
  for _ in range(lenth):
    str_list.append(main_url[randint(2,len(main_url)-2)])

  # Creating Short URL
  short_url = ''.join(str_list)
  
  # Returning the Dict of URL, Short Url and Domain.
  return {
    'short_url': short_url.lower(),
    'domain': domain,
    'url': url
  }