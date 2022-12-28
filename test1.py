import requests
from bs4 import BeautifulSoup  as bs

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs) # 앵커의 속성
# print(soup.a["href"]) # 앵커의 href 속성 값

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# print(soup.find(attrs={"class": "Nbtn_upload"}))

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling # rank2
# rank3 = rank2.next_sibling.next_sibling # rank3
# rank3.previousSibling.previousSibling #rank2
# rank1.parent #parent
# rank1.find_next_sibling("li") #rank2 개행같은 중간에 삽입된 문자 무시.
# rank1.find_next_siblings("li") # 복수개의 형제 값 조회

webtoon = soup.find("a", text="연애혁명-421. 원더랜드 (2)") #text value를 가지고 있는 태그 가져옴
print(webtoon)