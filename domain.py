from urllib.parse import urlparse

def get_domain_name( url ):
  try:
    results = get_subdomain_name( url ).split('.')
    return results[-2] + '.' + results[-1]
  except:
    return ''

def get_subdomain_name( url ):
  try:
    return urlparse( url ).netloc
  except:
    return ''

print ( get_domain_name( 'https://pygsheets.readthedocs.io/en/stable/' ) )
