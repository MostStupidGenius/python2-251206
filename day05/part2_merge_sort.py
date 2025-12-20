# part2_merge_sort.py
# 병합 정렬 알고리즘
# 병합 정렬은 퀵 정렬과 마찬가지로
# 분할 정복 알고리즘을 기반으로 구현된다.
# 퀵 정렬이 분할(divide)하면서 정렬(conquer)을 했다면
# 병합 정렬은 분할 따로, 정렬과 병합을 같이 하는 방식을 취한다.
# 때문에 병합 정렬 함수는 나누는 것과 반환하는 간단한 작업만 수행하며
# 두번째 함수인 병합 함수는 정렬된 데이터 리스트를 두 개 전달받아
# 이를 하나의 리스트로 병합하는 역할을 수행한다.

# 1. 병합 정렬 함수
# 병합 정렬 함수는 재귀함수로써 전달받은 데이터에 대해서
# 재귀적으로 정렬을 수행하는 역할을 한다.
def merge_sort(datas:list, show:bool=False, debug:bool=False):
    # 기본케이스
    # 길이가 1이하면 그대로 반환
    if len(datas) <= 1: return datas

    # 재귀케이스
    # 중앙 인덱스를 기준으로 좌우 리스트를 나눈다.
    mid_idx = len(datas) // 2
    # 좌우 나눠진 데이터 리스트는 슬라이스 기능을 이용하여 나눠준다.
    left = datas[:mid_idx] # 0번째(시작)부터 mid_idx-1번째 요소까지
    right = datas[mid_idx:] # mid_idx번째 요소부터 마지막 요소까지

    # 나눠진 데이터 리스트를 재귀적으로 merge_sort에 전달한다.
    sorted_left = merge_sort(left, show, debug)
    sorted_right = merge_sort(right, show, debug)

    # 정렬된 좌우의 데이터 리스트를 merge 함수에 전달하여
    # 하나의 정렬된 리스트로 병합한다.
    # ※ 좌우 데이터 리스트들은 모두 정렬된 상태라고 가정한다.
    result = merge(sorted_left, sorted_right, show, debug)

    if show: print(f"merge_sort:\n\t{result}")

    # debug가 True이면 엔터를 입력하여 다음 코드를 진행한다(pause)
    if debug: input("엔터를 입력해 진행해주세요")

    # result 변수는 병합된 정렬 리스트다.
    return result

# 2. 병합 함수
def merge(left:list, right:list, show:bool=False, debug:bool=False) -> list:
    # 전달받는 left 매개변수와 right 매개변수가 모두
    # 정렬된 데이터 리스트라고 가정하고 이를 정렬하며 병합하는 동작을 수행한다.
    # merge 함수의 결과로 정렬된 하나의 데이터 리스트가 반환된다.
    
    # 결과를 담을 리스트 선언
    # 이때 전달받은 좌우 데이터 리스트의 총 개수만큼 공간을 미리 만든다.
    result = [0] * (len(left) + len(right))
    # [0, 0, ..., 0]

    # 좌우 데이터 리스트의 현재 비교 대상 인덱스를 관리할 변수 선언
    left_idx, right_idx = 0, 0
    # 0번째 요소부터 해당 리스트의 길이-1번째 요소까지 순차적으로 확인하며
    # 두 리스트의 요소를 비교할 것이다.
    # 비교 결과 더 작은 값이 새로운 리스트 result에 적절한 위치에 담기고
    # 해당 데이터 리스트의 인덱스가 1 증가하여 다음 요소를 가리킬 것이다.
    # 삽입할 위치의 인덱스를 관리할 변수는 따로 만들지 않고
    # left_idx와 right_idx를 더한 값으로 대신한다.

    # 좌우 데이터 리스트의 길이보다 각각의 현재 보는 인덱스(left_idx,..)의
    # 크기가 작은 동안 무한 반복한다.
    while left_idx < len(left) and right_idx < len(right):
        # 만약 left_idx의 요소가 right_idx의 요소보다 작다면
        if left[left_idx] < right[right_idx]:
            # 그 값을 left_idx + right_idx 번째 result의 요소에 저장한다.
            result[left_idx+right_idx] = left[left_idx]
            # 왼쪽에서 현재 가리키는 요소의 인덱스를 1 증가 시켜
            # 다음 요소를 가리키게 한다.
            left_idx += 1
        # 만약 오른쪽 현재 보고 있는 요소가 더 작다면
        else:
            result[left_idx+right_idx] = right[right_idx]
            right_idx += 1
        # 정렬 결과 출력
        if show:
            print(f"merge({left_idx}, {right_idx}):")
            print(f"\t{result}")
        if debug:
            input("엔터를 눌러 진행")
    
    # while문을 탈출했다는 것은, 두 데이터 리스트 중 하나의 모든 요소를
    # result에 담았다는 의미이다.
    # 만약 모든 요소를 소모하지 못한 리스트가 남았다면
    # 이를 result 뒷부분에 붙여주어야 한다.
    # 왜? 남은 데이터는 두 데이터 리스트를 통틀어 가장 큰 값 그룹에 속하기 때문이다.

    # 왼쪽 리스트의 인덱스가 길이보다 작은 동안 남은 요소를
    # result에 추가한다.
    while left_idx < len(left):
        # 남은 요소 추가
        result[left_idx + right_idx] = left[left_idx]
        left_idx += 1
    # 오른쪽 리스트도 동일하게 동작시킨다.
    while right_idx < len(right):
        # 남은 요소 추가
        result[left_idx + right_idx] = right[right_idx]
        right_idx += 1
    # 남은 요소까지 모두 담겼다면
    # 해당 result를 반환한다.
    return result
    
if __name__ == "__main__":
    import random as r
    datas = list(range(10))
    r.shuffle(datas)
    print(datas)
    result = merge_sort(datas, True, True)
    print(result)