#web1.py

from bs4 import BeautifulSoup

#페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#검색이 용이한 스프객체 (html태그 파싱)
soup = BeautifulSoup(page, "html.parser")
#전체보기
#print(soup.prettify())
#<p>전체 검색
#print(soup.find_all("p"))
#<p>첫번째 태그만 검색
#print(soup.find("p"))
#조건검색: <p vlass="outer-text">
#print(soup.find_all("p", class_="outer-text"))  #이름충돌을 위하여 class_ 사용
#attibutes ==> attrs
#print( soup.find_all("p", attrs={"class":"outer-text"}) )
#내부의 문자열만 검색
for tag in soup.find_all("p"):
    #text속성을 지정
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)