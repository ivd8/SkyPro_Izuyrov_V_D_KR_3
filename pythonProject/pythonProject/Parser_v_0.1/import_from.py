import requests
#from bs4 import BeautifulSoup
#import lxml

#url = 'https://tracksino.com/dreamcatcher?period=1month'
response = requests.get('https://api.tracksino.com/dreamcatcher_history?filter=&sort_by=&sort_desc=false&page_num=1&per_page=10&period=1month')
print(response)