# DemoDict.py

#사전식 구조
colors = {"apple":"red", "banana":"yellow"}
print(colors)
print(len(colors))

#검색
print(colors["apple"])
#임력
colors["cherry"] = "red"
print(colors)
#수정
colors["apple"] = "pink"
#삭제
del colors["banana"]
print(colors)

#반복문
for item in colors.items():
    print(item)

print("---key, value---")
for k,v in colors.items():
    print(k,v)
