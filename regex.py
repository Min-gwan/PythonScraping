#정규식 라이브러리
import re

# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...


# . : 하나의 문자 (ca.e) > care, cafe, case
# ^ : 문자열의 시작 (^de) > desk, destination
# $ : 문자열의 끝 (se$) > case, base
# group() : 일치하는 문자열 반환
# string : 입력받은 문자열
# start() : 일치하는 문자열의 시작 index
# end() : 일치하는 문자열의 끝 index
# span() : 일치하는 문자열의 시작/끝 index
# match() : 주어진 문자열의 처음부터 일치하는지 확인
# search() : 주어진 문자열 중에 일치하는게 있는지 확인
# findall() : 일차하는 모든 것을 리스트 형태로 반환

p = re.compile("ca.e") #pattern

m = p.match("case")
# # print(m)
# # print(m.group()) # 매치되지 않으면 에러 발생
# if m:
#     print(m.group())
# else:
#     print("매칭되지 않음")

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")
print_match(m)

# more information W3school, python re(document)