import requests
from bs4 import BeautifulSoup as bs

url = 'https://search.shopping.naver.com/book/search/category?bookTabType=ALL&catId=50005552&pageIndex=1&pageSize=40'
response = requests.get(url)
soup = bs(response.text, "lxml")
