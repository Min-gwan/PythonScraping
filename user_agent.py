import requests

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
response = requests.get(url,headers=headers)
response.raise_for_status()
with open("naver_news.html", "w", encoding="utf8") as f:
    f.write(response.text)

# user agent string - what is my user agent
"""
브라우저 별로 user agent가 다름 
"""

# pip install lxml