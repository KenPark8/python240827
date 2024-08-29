#DemoForm2.py

#DemoForm2.ui(화면단) + DeomForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

#디자인 파일 요청(파일명 변경)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindow)
class DemForm(QMainWindow, form_class):
    #초기화 루틴
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면 출력")
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)

        #검색을 할 soup객체 생성
        soup = BeautifulSoup(response.text, "html.parser")

        #파일로 저장(wt, a+)
        f = open("daangn.txt", "a+", encoding="utf-8")

        posts = soup.find_all("div", attrs={"class":"card-desc"})
        f.write("\n\n")
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            addrElem = post.find("div", attrs={"class":"card-region-name"})
            #문자열만 추출
            title = titleElem.text.strip()
            price = priceElem.text.strip()
            addr = addrElem.text.strip()
            #f-string
            print(f"{title}, {price}, {addr}")
            f.write(f"{title}, {price}, {addr}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

#직접 모듈을 실행했는지를 체크(진입점 체크)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemForm()
    demoForm.show()
    app.exec_()
