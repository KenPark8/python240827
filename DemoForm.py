#DemoForm.py
#DemoForm.ui(화면단) + DeomForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일 요청
form_class = uic.loadUiType("DemoForm.ui")[0]

#윈도우 클래스 정의
class DemForm(QDialog, form_class):
    #초기화 루틴
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면 출력")

#직접 모듈을 실행했는지를 체크(진입점 체크)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemForm()
    demoForm.show()
    app.exec_()
