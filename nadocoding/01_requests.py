import requests
res = requests.get("https://google.com")
print("응답 코드 : ", res.status_code ) #200이면 정상

if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. 에러코드 : ", res.status_code)

res.raise_for_status() #문제가 생기면 바로 종료
print("웹 스크래핑을 진행")

print(len(res.text))
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
