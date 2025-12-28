# programmers_43165.py

# 문제 설명
# n개의 음이 아닌 정수들이 있습니다. 
# 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 
# 타겟 넘버를 만들려고 합니다. 
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 
# 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 
# 타겟 넘버 target이 매개변수로 주어질 때 
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 
# 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5
# [4, 1, 2, 1]	    4	    2
# 입출력 예 설명
# 입출력 예 #1

# 문제 예시와 같습니다.

# 입출력 예 #2

# +4+1-2+1 = 4
# +4-1+2-1 = 4
# 총 2가지 방법이 있으므로, 2를 return 합니다.

# DFS(깊이우선탐색)
# stack, 재귀함수 방식
def solution(numbers, target):
    return DFS(numbers[0], 0, numbers, target) +\
        DFS(-numbers[0], 0, numbers, target)

# 깊이우선탐색 함수
def DFS(num, order, numbers, target):
    """
    재귀적으로 이진트리를 탐색하여 해당 라인의 총합이 target과 같은 조합의 개수를 반환
    :param num: 현재 노드의 값 설정
    :param order: 이진트리의 깊이
    :param numbers: 전체 데이터 배열(리스트)
    :param target: 해당 조합의 총합이 이 target과 같아야 한다.
    """
    # 만약에 order가 전체 길이-1이라면 마지막 노드(리프 노드)라는 의미이다
    # -> 기본 케이스
    if order == len(numbers) - 1: # 자식이 없는 노드
        # num이 target과 같은 경우 1을 반환
        if num == target:
            return 1
        return 0
    
    # 왼쪽 서브트리에서의 해당 조합이 맞는 경우와 오른쪽 서브트리의 합을 반환
    left = DFS(num + numbers[order+1], order+1, numbers, target)
    right = DFS(num - numbers[order+1], order+1, numbers, target)
    return left + right

# BFS(너비우선탐색)
def solution(numbers, target):
    # list를 활용하여 Queue 자료구조로 너비우선탐색 수행
    answer = 0
    
    # 탐색할 순서를 저장할 queue 리스트를 생성
    q = []
    # queue 자료구조의 값은 해당 numbers의 요소 값과 인덱스 값을 tuple 형태로 저장
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    # while문을 활용하여 q가 빌 때까지 너비우선탐색 수행
    while q:
        # 현재 값과 인덱스를 .pop()으로 언패킹
        num, order = q.pop(0) # FIFO

        # 만약에 현재 순서가 마지막 순서라면
        if order == (len(numbers) - 1):
            # 그리고 num의 값이 target과 같다면 그 카운트를 1 추가한다.
            if num == target:
                answer += 1
            # answer += (num == target)
            continue
        # 현재 값이 마지막 순서가 아니라면 다음 순서를 추가한다.
        q.append((num + numbers[order+1], order+1))
        q.append((num - numbers[order+1], order+1))
    return answer

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3) == 5)
    print(solution([4, 1, 2, 1], 4) == 2)