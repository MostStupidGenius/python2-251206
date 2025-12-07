# part3_regular_expression.py
# 정규표현식
# 정규표현식이란, 아스키코드 상의 문자를 활용하여
# 문자열 검색, 대체, 반복, 캡쳐 등의 문자열 고급 처리 기능을 도와주는 기술이다.
# 정규표현식은 파이썬 뿐만 아니라 현대에 쓰이는 대부분의 IT영역에서 공통적으로 쓰이며
# 한번 배워두면 약간의 학습과 응용으로 다른 영역에서 사용할 수 있다.
# 사용처: 일반적으로 유효성 검사(validation), 문자열 대체(replace), 검색 등에
# 사용된다.
# 고급사용처: 초성검색

import re

def find_number():
    # 정규표현식을 사용하여 숫자, 문자, 특수기호 등을 검색하고 추출해보자.
    # 1. 숫자를 나타내는 정규표현식은 r'\d'이고 한 번 이상 반복된다면 +를 붙인다.
    pattern = re.compile(r"\d+") # 숫자의 반복을 찾아내는 패턴 컴파일

    text = "123a45b13420c"
    
    # 위 텍스트에서 컴파일된 패턴을 모두 찾으려면
    # .findall()에 text를 전달하면 된다.
    matches = pattern.findall(text)
    print(matches)

def test2():
    pattern = re.compile(r"[가-힣]+로\s?\d+번?길")
    p2 = re.compile(r"\d+\-?\d+\([가-힣]+\)")
    # 정규표현식 내에서 +, -, ? 등의 역할이 이미 주어진 특수기호를 사용하고자 할 때에는
    # 그 앞에 백슬래시\를 넣어서 escape해주어야 한다.
    text = "경상남도 김해시 삼안로184번길 10-11(삼방동)"
    matches = pattern.findall(text)
    print(matches)
    m2 = p2.findall(text)
    print(m2)

# 전화번호 3, 4, 4 총 11자리의 숫자를 추출하는 기능
def extract_phone_number(phone_number:str):
    # case1: 010-1234-1234
    # case2: 010 1234 1234
    # case3: 01012341234
    # case4: 010.1234.1234
    # 위 경우를 보면 숫자3개, 숫자4개, 숫자4개로 이루어져있다.
    # 각 숫자 사이에 숫자가 아닌 무언가가 있을 수도 없을 수도 있다.
    pattern = re.compile(r"(\d{3})(?:[^0-9]*)(\d{4})(?:[^0-9]*)(\d{4})")
    matches = pattern.findall(phone_number)
    for match in matches:
        print(match)

if __name__ == "__main__":
    # find_number()
    # test2()
    extract_phone_number("010 1234 1234")
    print("=" * 20)
    extract_phone_number("010-1234-1234")
    print("=" * 20)
    extract_phone_number("01012341234")
    print("=" * 20)
    extract_phone_number("010.1234.1234")
    pass