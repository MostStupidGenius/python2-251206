# part1_heap_sort.py
# 힙정렬 알고리즘
# 힙정렬은 최대heap구조를 기반으로 정렬을 하는
# 알고리즘이다.
# 최대heap구조란, 가장 위에 있는 루트 노드의 값을
# 최대로 유지하기 위해 자식노드와 부모노드의 크기 관계를
# 설정하는 것을 가리킨다.
# 최대heap구조를 유지하면 0번째 요소(루트)의 값이
# 전체 데이터 중 가장 큰 값이 되게 된다.
# 이 최대값을 마지막 요소와 교환하고 데이터 길이를 줄인 뒤
# 남은 요소에 대해서 heapify를 진행하여 heap구조로 되돌리는
# 방식으로 정렬이 진행된다.

# 필요한 함수 2가지
# 1. heap_sort
# - 전달된 데이터에 대해서 마지막 비단말노드부터 순차적으로
# 최대 힙 구성 단계를 진행한다.
# - 정렬을 진행한다.
# 2. heapify
# - 최대 힙속성을 유지하기 위해 전체 데이터와 정렬할 데이터의 길이,
#   현재 가리키고 있는 루트 노드 인덱스 등을 전달하여 
#   최대 힙 구조로 바꾸는 역할을 한다.
# - 이는 정렬을 진행할 때마다 호출된다.

def heap_sort(datas:list, show:bool=False)->list:
    """
    :param datas: 여러 개의 숫자 데이터가 담긴 정렬 되지 않은 리스트
    :type datas: list
    :param show: 정렬되는 과정의 데이터 리스트를 출력할지 여부
    :type show: bool
    :return: 정렬된 datas 객체
    :rtype: list
    """
    # 1. 전달받은 정렬되지 않은 데이터를 최대 힙으로 구성한다.
    # 이때 전체 데이터의 길이를 먼저 추출한다.
    length = len(datas)

    # 2. 최대 힙 구성단계
    # 마지막 비단말노드부터 -1씩 이동하여 루트 노드까지 순차적으로 heapify를 진행한다.
    # why? 단말노드에는 heapify를 진행하는 것이 의미가 없기 떄문이다.
    # 마지막 비단말노드를 구하는 공식은 `길이//2 - 1`
    마지막_비단말노드_인덱스 = length//2 - 1
    for current_length in range(마지막_비단말노드_인덱스, -1, -1):
        # 마지막 비단말 노드 인덱스부터 -1까지 -1씩 증가하며
        # 최초의 최대 힙 구성
        heapify(datas, length, current_length)
        # heapify에는 전체 데이터와 정렬 대상이 되는 데이터의 길이,
        # 그리고 현재 정렬 대상이 되는 비단말 노드의 인덱스
        # 마지막 정렬 대상은 i == 0이 되는 루트노드까지 진행된다.
    
    # 3. 정렬 단계
    # 최대값이 된 0번째 노드, 즉 루트 노드의 값과 마지막 노드의 값을
    # 교환하고 데이터의 길이를 1만큼 줄인 뒤, 다시 heap구조로 되돌린다.
    # 이를 데이터 길이가 1이 될 때까지 반복한다.
    for current_length in range(length-1, 0, -1):
        # 마지막 인덱스부터 1번째 인덱스([1])까지 반복적으로 진행.
        # 이는 정렬된 데이터를 전체 길이에서 제외하기 위한 반복 방식이다.
        # 루트(최대값)과 현재 힙의 마지막 요소를 서로 교환
        # ※ 현재 힙의 마지막 요소라는 것은,
        #    정렬되지 않은 데이터 중 마지막이라는 의미이다.
        datas[0], datas[current_length] = datas[current_length], datas[0]

        if show: print(datas[:current_length], datas[current_length:])
        # 루트 노드에 대해서 heapify를 수행하여 최대 힙 속성 복구
        # 두번째 매개변수는 datas에서 정렬되지 않은 데이터의 길이를 가리킨다.
        # 마지막 매개변수는 루트노드부터 진행됨을 가리킨다.
        heapify(datas, current_length, 0, show)
    return datas

def heapify(datas:list, length:int, current_idx:int, show:bool=False):
    """
    :param datas: 정수값들이 담긴 정렬 되지 않은 부분의 리스트
    :type datas: list
    :param length: 0번째노드부터 length번째 노드까지 정렬을 진행하겠다는 의미
    :type length: int
    :param current_idx: datas 중 현재 정렬 대상이 되는 부모 노드의 인덱스
    :type current_idx: int
    """
    # 전달받은 current_idx를 가장 큰 값을 가진 인덱스로 취급한다.
    largest_idx = current_idx

    # 왼쪽 자식 인덱스는 현재 인덱스 * 2 + 1의 값을 가진다.
    left_idx = current_idx * 2 + 1
    right_idx = left_idx + 1
    
    # ==================================
    # 왼쪽 자식이 힘 크기 범위 내에 있고(길이 제한),
    # 현재 largest_idx의 값보다 큰 경우
    if left_idx < length and datas[left_idx] > datas[largest_idx]:
        largest_idx = left_idx
    # 오른쪽 자식도 동일하게 진행
    # 이때 위의 왼쪽 자식 작업과 독립적으로 수행해야 한다.
    if right_idx < length and datas[right_idx] > datas[largest_idx]:
        largest_idx = right_idx
    # ==================================
    # 다른 방식으로 구현해보기
    # targets = [left_idx, right_idx, current_idx]
    # d = [datas[i] for i in targets]
    # largest_value = max(d)
    # largest_idx = d.index(largest_value)
    
    # 초기의 largest_idx의 값과 현재 세팅된 largest_idx의 값이 다르다면
    # 루트 노드보다 더 큰 값이 있다는 의미이므로 교환이 필요하다
    if largest_idx != current_idx:
        datas[largest_idx], datas[current_idx] = \
            datas[current_idx], datas[largest_idx]
        # 교환이 일어났으므로 해당 largest_idx 위치를 기준으로
        # heapify를 재귀적으로 다시 수행해야 한다.
        if show: print(f"\t{datas[:largest_idx]}", datas[largest_idx:])
        heapify(datas, length, largest_idx)
    # 기본케이스
    # 최초의 값과 최종 값이 같다면 교환이 필요없으므로
    # 함수를 재귀적으로 호출하지 않는다.

if __name__ == "__main__":
    import random as r
    datas = list(range(10))
    r.shuffle(datas)
    print(f"정렬전:\n{datas}")
    datas = heap_sort(datas, 0)
    print(f"정렬완료:\n{datas}")

# =============
# d = [datas[i] for i in [left_idx, right_idx, current_idx]]
# largest_idx = d.index(max(d))