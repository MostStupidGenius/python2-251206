# part2_insertion_sort.py
# 삽입 정렬
# 첫번째 요소를 정렬된 것으로 취급하면서 시작을 하고,
# 정렬된 부분과 정렬이 안 된 부분을 나눠서 
# 정렬이 안 된 첫번째 요소를 정렬된 요소들과 비교하여
# 적절한 위치에 삽입하는 정렬 알고리즘이다.

def insertion_sort(datas:list, show:bool=False) -> list:
    # 전체 데이터의 길이를 변수에 저장해둔다.
    length = len(datas)
    # 0번째 요소는 이미 정렬된 것으로 취급하기 때문에
    # 1번째 요소부터 length-1번째 요소까지 path를 반복한다.
    for i in range(1, length):
        # 현재 정렬 안 된 부분에서 삽입하려는 대상 값
        key = datas[i]
        # 현재 숫자의 이전 위치를 변수에 담아서 반복문을 통해
        # 정렬된 부분을 탐색하여 적절한 위치를 찾아 들어간다.
        j = i - 1
        # j 인덱스를 1씩 감소하며 정렬된 부분을 탐색할 것이다.
        # 그렇다는 말은, j는 반드시 0보다 크거나 같아야 하며
        # j 인덱스를 감소시킨다는 것은, j번째에 있는 값이 key보다 작다는 뜻이다.
        while j >= 0 and key < datas[j]:
            # 현재 탐색하고 있는 값을 그 오른쪽 위치에 똑같이 저장한다.
            datas[j+1] = datas[j]
            j -= 1 # j인덱스를 감소시킴으로써, 정렬된 부분에서 왼쪽(작은쪽)으로
            # 시선을 옮긴다.
        # 탐색하는 반복문을 탈출했다는 것은 자기 자리를 찾았다는 것이므로
        # j번째에 key값을 넣어야 하지만,
        # 탐색 반복문에서 마지막에 -1을 했기 때문에 1을 증가시킨 위치에 key를 삽입한다.
        datas[j+1] = key
        if show: print(datas)
    return datas

if __name__ == "__main__":
    # 셔플을 위한 랜덤 임포트
    import random as r
    datas = list(range(10))
    # 섞기
    r.shuffle(datas)
    # 섞인 데이터 출력
    print(datas)

    # 정렬 알고리즘 사용
    insertion_sort(datas, True)

    # 정렬 결과 출력
    print(f"정렬완료\n{datas}")