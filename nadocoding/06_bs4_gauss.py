import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 만화 제목 + 링크 출력력
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print(link)
# for cartoon in cartoons:
#     print(cartoon.a.get_text())
#     print("https://comic.naver.com" + cartoon.a["href"])


# 만화 평점 평균균
ratings = soup.find_all("div", attrs={"class":"rating_type"})
total = 0
for rating in ratings:
    total += float(rating.strong.get_text())
print("전체 점수:",total)
print("평점 평균:",total/len(ratings))
