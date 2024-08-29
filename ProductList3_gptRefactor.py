import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

class ProductDB:
    def __init__(self, db_name="ProductList.db"):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self._initialize_db()

    def _initialize_db(self):
        # 테이블이 없으면 생성
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute(
            "UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (name, price, prod_id)
        )
        self.con.commit()

    def remove_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id = ?;", (prod_id,))
        self.con.commit()

    def get_all_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

    def close(self):
        self.con.close()

#디자인 파일을 로딩
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)

        self.db = db

        # 초기값 셋팅
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget의 컬럼폭 셋팅하기
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        # QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])

        # QLineEdit으로 수정함
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 초기 데이터 로드
        self.getProduct()

    def addProduct(self):
        # 입력 파라메터 처리
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        self.db.add_product(self.name, int(self.price))
        # 리프레시
        self.getProduct()

    def updateProduct(self):
        # 업데이트 작업시 파라메터 처리
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        self.db.update_product(int(self.id), self.name, int(self.price))
        # 리프레시
        self.getProduct()

    def removeProduct(self):
        # 삭제 파라메터 처리
        self.id = self.prodID.text()
        self.db.remove_product(int(self.id))
        # 리프레시
        self.getProduct()

    def getProduct(self):
        # 검색 결과를 보여주기 전에 기존 컨텐트를 삭제 (헤더는 제외)
        self.tableWidget.clearContents()
        products = self.db.get_all_products()
        
        # 행숫자 카운트
        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 인스턴스를 생성한다.
app = QApplication(sys.argv)
db = ProductDB()
myWindow = Window(db)
myWindow.show()
app.exec_()
db.close()
