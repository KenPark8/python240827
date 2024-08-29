#web2.py

#웹서버와 통신
import requests
#크롤링
from bs4 import BeautifulSoup

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


# <div class="card-desc">
#       <h2 class="card-title">맥북 m1 프로 pro 13인치 램8gb / 512gb [96%]</h2>
#       <div class="card-price ">
#         280,000원
#       </div>
#       <div class="card-region-name">
#         서울 영등포구 영등포동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 74
#           </span>
#         ∙
#         <span>
#             채팅 104
#           </span>
#       </div>
#     </div>