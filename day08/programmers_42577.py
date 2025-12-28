# programmers_42577.py
# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.
# 입출력 예제
# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false
# 입출력 예 설명
# 입출력 예 #1
# 앞에서 설명한 예와 같습니다.

# 입출력 예 #2
# 한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

# 입출력 예 #3
# 첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.
def solution(phone_book):
    # 1. 문자열 길이가 짧은 것부터 정렬하여 더 긴 다른 전화번호의 앞부분을 그 길이만큼 슬라이싱하여 비교
    # 길이 오름차순으로 정렬
    phone_book.sort(key=len)

    # for문을 이용하여 0번째 요소부터 순차적으로 순회
    for i, e in enumerate(phone_book):
        # 내부 for문은 i+1번째 요소부터 마지막 요소까지 현재 e 번호가
        # 접두사로 존재하는지를 검사하는 반복문이다.
        for j in range(i+1, len(phone_book)):
            # e 번호 이후의 전화번호부터 마지막 번호까지 순회하며 검사
            if phone_book[j].startswith(e):
                return False

    return True

    # 2. 정규표현식의 시작을 나타내는 "^"와 짧은 전화번호를 조합하여 해당 패턴을 가진 전화번호가 있는지를 찾는 방법

# 두번째 시도
# 위의 이중 반복문으로는 효율성이 떨어진다.
# 다른 방법을 알아보자.
def solution(phone_book):
    # 하나의 for문으로 가능할까?
    # 모든 문자열을 오름차순으로 정렬
    phone_book.sort()
    # ["119", "119552",...]
    # i번째 요소와 i+1번째 요소를 바로 비교
    for i in range(len(phone_book) - 1):
        # 두 요소를 비교
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# 3번
# 리스트 컴프리헨션으로 압축해보기
def solution(phone_book):
    # 하나의 for문으로 가능할까?
    # 모든 문자열을 오름차순으로 정렬
    phone_book.sort()
    # result는 해당 요소가 다음 요소의 접두사인지 여부를 리스트로 담은 결과다.
    result = [phone_book[i+1].startswith(phone_book[i]) for i in range(len(phone_book) - 1)]
    return bool(not max(result))

if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]) == False)
    print(solution(["123","456","789"]) == True)
    print(solution(["12","123","1235","567","88"]) == False)