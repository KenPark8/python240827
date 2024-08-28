# db1.py
import sqlite3

#연결객체 생성
#con = sqlite3.connect(":memory:")
#파일에 저장(IDLE 같이 연습)
con = sqlite3.connect(r"c:\work\sample.db")

#SQL구문을 실행하는 커서 객체 생성
cur = con.cursor()
#테이블 구조 생성(체크코드 추가)
cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

#입력 구문
cur.execute("insert into PhoneBook values('derick', '010-123');")
#입력 매개변수 처리
name = '전우치'
PhoneBook = '010-2323'
cur.execute("insert into PhoneBook values(?,?);", (name, PhoneBook))

#다중행을 입력
datalist = (("이순신","010-2323"), ("홍길동","010-1123"))
cur.executemany("insert into PhoneBook values(?,?);",  datalist)

#검색 구문
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#블럭을 주석: ctrl + /
# print("---fetchone()---")
# print(cur.fetchone())
# print("---fetchmany(2)---")
# print(cur.fetchmany(2))
# print("---fetchall()---")
# print(cur.fetchall())
    
