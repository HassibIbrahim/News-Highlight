import urllib.request,json
from .models import News, Headlines  

# Getting api key 
api_key = None

# Getting the news base url
base_url = None       

# Getting news secondary url 
secondary_url = None    

def configure_request(app):
    global api_key,base_url,secondary_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    secondary_url = app.config['NEWS_API_SECONDARY_URL']
