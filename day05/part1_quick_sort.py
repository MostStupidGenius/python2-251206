# part1_quick_sort.py
# 퀵 정렬 알고리즘
# 퀵 정렬 알고리즘은 분할 정복 알고리즘을 기반으로 하여
# 전체 데이터를 pivot이라는 기준값을 선정하여 이를 기준으로 작은 값과
# 큰 값으로 구분하여 분류하는 방식을 취한다.
# 이렇게 나누다보면 더 이상 쪼갤 수 없는 순간이 온다.
# 이때부터 다시 병합(merge)하여 최종 결과를 도출하는 것으로
# 큰 문제를 작은 문제로 쪼개어 해결할 수 있다.

# 이러한 퀵 정렬은 재귀함수(recursive function) 방식으로 구현할 수 있다.

# 재귀함수
# 재귀함수는 2가지 케이스가 존재해야 정상적으로 동작한다.
# 1. 기본 케이스
#   재귀함수의 재귀동작을 중단할 조건에 따라 재귀를 중단시키는 기본 케이스
# 2. 재귀함수를 동작시키는 재귀케이스
def quick_sort(datas:list) -> list:
    # 기본 케이스
    # 전달받은 데이터의 요소 개수가 1개 이하이면 정렬할 필요가 없으므로
    # 그대로 반환한다.
    if len(datas) <= 1: return datas

    # 재귀케이스
    # 1. 피벗을 선택한다.
    pivot = datas[0] # 피벗 선택의 규칙은 없다.
    # 하지만 가능한 한 데이터 중 중앙값을 선택하면 효율적으로 동작한다.
    
    # 2. 피벗을 기준으로 피벗과 같은 값(middle), 작은 값(left), 큰값(right) 등
    # 총 3개의 그룹으로 나눈다.(오름차순)
    left = [e for e in datas if e < pivot] # 피벗보다 작은 값들
    mid = [e for e in datas if e == pivot] # 최소 하나의 요소는 포함된다.
    right = [e for e in datas if e > pivot] # 피벗보다 큰 값들

    # 3. 나눠진 mid를 제외한 그룹들에 대해서 재귀적으로 이 동작을 반복한다.
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # 4. 정렬된 좌우 그룹을 피벗 그룹과 병합한다.
    result = sorted_left + mid + sorted_right # 리스트끼리의 덧셈연산은
    # 하나의 리스트로 병합하는 기능을 한다.

    # 5. 병합된 최종 결과를 반환한다.
    return result


if __name__ == "__main__":
    pass