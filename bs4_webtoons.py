import requests
from bs4 import BeautifulSoup as bs

url1 = 'https://comic.naver.com/webtoon/weekday'
url2 = 'https://comic.naver.com/webtoon/list?titleId=799793'
res = requests.get(url2)
res.raise_for_status()

soup = bs(res.text, 'lxml')
# 네이버 웹툰 전체 목록 가져오기
# cartoons = soup.find_all("a", attrs={'class':'title'})
# for cartoon in cartoons:
#     print(cartoon.get_text())

# test = soup.select_one('#content > div.list_area.daily_all > div:nth-child(2) > div > ul > li:nth-child(1) > a')
# print(test.text)

# cartoons = soup.find_all('td', attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title, "https://comic.naver.com"+link)
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수:",total_rates)
print("평균 점수 ",total_rates / len(cartoons))

# soup.prettify() 문서 정리

headers = {
    "User-Agent":"value",
    "Accept-Language":"ko-KR,ko" # 한글 페이지 반환 요청
}

# soup.find_all("element", attrs={"class":["A, B"]}) 클래스가 A or B인 경우를 찾음
