# 파이썬 심화과정
#  - 웹 크롤링: 웹 페이지에서 원하는 데이터를 수집
#  - 모듈: Beautifulsoup4, selenium, requests

# - 데이터 수집!

# 인공지능 개발 과정
#  1.데이터 수집
#  2.데이터 저장
#  3.탐색적 데이터 분석(EDA)
#  4.데이터 전처리
#  5.데이터 변환
#  6.베이스라인 모델 개발
#  7.성능 향상
#  8.시각화
#  9.배포 및 서비스

# 웹 서비스
#  - HTML(메인), CSS, Javascript : 웹 표준


# Daum News의 제목, 본문 수집 코드

import requests
from bs4 import BeautifulSoup

# requests: 웹사이트 코드 복사 Get
# BeautifulSoup: requests Get 해온 코드에서 필요한 정보만 find해서 가져오기

url = "https://v.daum.net/v/20230509090530015"  #수집할 페이지 주소
result = requests.get(url)

# 웹 브라우저                    다음 서버
#          request----->
#                <-------response
# response[200]: success
# reponse[400~500]: fail
#print(result)
#print(result.text)

# requests로 가져온 코드 -> BeautifulSoup 접근 가능한 코드로 변경
doc = BeautifulSoup(result.text, "html.parser")
title = doc.select("h3.tit_view")[0].get_text()
# [0]은 리스트를 벗김, .get_text()는 텍스트만 가지고 옴
contents = doc.select("section > p")  # section 태그 안에 있는 p 태그들
print("=" * 100)
print(f"뉴스제목: {title}")
print("=" * 100)
content = ""  # 전체 본문을 담을 변수
contents.pop(-1)
for tag in contents:
   content = content + tag.get_text()
print(f"뉴스본문: {content}")
