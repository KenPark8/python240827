#web1.py

from bs4 import BeautifulSoup

#페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#검색이 용이한 스프객체
soup = BeautifulSoup(page, "html.parser")
#전체보기
print(soup.prettify())