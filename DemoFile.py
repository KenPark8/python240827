#DemoFile.py

#끄기
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째 라인\n두번째 라인\n세번째 라인\n")
f.close()

#읽기 (raw string notation)
f = open (r"c:\work\test.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()