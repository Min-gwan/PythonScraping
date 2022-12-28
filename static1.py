import requests

url = 'https://www.naver.com/'
url2 = 'https://nadocoding.tistory.com/'
url3 = 'https://www.google.com/'
response = requests.get(url3)
print("응답코드 :", response.status_code)

if response.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ",response.status_code, "]")

# 앞선 if문을 함수화 시킨 것
# response.raise_for_status()

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(response.text)

