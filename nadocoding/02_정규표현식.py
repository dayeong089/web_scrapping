# 주민등록번호
# 000809-1111111

# 이메일 주소
# nadocoding@gmail.com

# 차량 번호
# 123가 1233

# ip 주소
# 192.168.0.1

import re
#ca?e
p = re.compile("ca.e") 
# .:하나의 문자 > ca.e : care, cafe, case
# ^:문자열의 시작 > (^de) : desk, deeeek
# $:문자열의 끝 > (se$) : case, vase
p2 = re.compile("^de")
p3 = re.compile("se$")

def print_match(m):
    if m:
        print("group: ", m.group()) # 매치되면 print, 매치되지 않으면 error, 일치하는 문자열 반환
        print("string: ", m.string) # 입력받은 문자열 반환
        print("start: ", m.start()) # 일치하는 문자열 시작 index
        print("end: ", m.end()) # 일치하는 문자열의 끝 index
        print("span: ", m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print('매칭되지 않음')

m = p.match("case") # 주어진 문자열 처음부터 일치하는지 확인
m2 = p.match("good care")
m3 = p.match("careless")
print_match(m) # case
print_match(m2) # error
print_match(m3) # careless

m4 = p2.match("desk")
print_match(m4)
m5 = p3.match("case")
print_match(m5)

n = p.search("good care") # 주어진 문자열 중 일치하는 것이 있는가
print_match(n)

lst = p.findall("good care cafe") # 일치하는 모든 것을 리스트 형식으로 반환
print(lst) # ['care', 'cafe']

# 1. p = re.compile("원하는 형태") 
# 2. m = p.match("비교할 문자열") 주어진 문자열 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") 주어진 문자열 중 일치하는 것이 있는가
# 4. lst = p.findall("비교할 문자열") 일치하는 모든 것을 리스트 형식으로 반환


# 이런식으로 사용
# items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# li tag 중 search_product로 시작하는 class
