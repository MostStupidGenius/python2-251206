# part1_selection_sort.py
# 선택 정렬
# 정렬된 부분과 정렬이 안 된 뒷부분으로 나누어서
# 정렬이 안 된 부분 중 가장 작은 값의 인덱스를 찾아
# 현재 정렬이 안 된 부분의 첫번째 요소와 교환한다.
# 그 다음 정렬 때에는 정렬된 부분은 제외하고 정렬이 안 된 부분에 대해서
# 이를 반복한다.

# 선택 정렬 함수
def selection_sort(datas:list, show:bool=False) -> list:
    # 전달받은 데이터의 전체 길이를 변수에 저장한다.
    length = len(datas)
    # 전체 길이 만큼 정렬의 시행을 반복한다.
    # 이를 패스(path)라고 부른다.
    for i in range(length):
        # 외부 반복문의 역할:
        # 배열 전체를 반복하며 i번째 위치를 가리킨다.
        # 내부 반복문을 통해서 찾아낸 가장 작은 값이 i번째 위치와 맞바뀐다.
        # 가장 작은 값의 인덱스를 현재 i번째 위치로 초기화한다.
        min_index = i
        # 내부 반복문
        # 내부 반복문은 i+1번째 요소부터 마지막 요소까지 검사하여
        # 가장 작은 값의 인덱스를 찾는 반복문이다.
        for j in range(i+1, length):
            # 만약 j번째 요소가 min_index 번째 요소보다 작다면
            if datas[j] < datas[min_index]:
                # 가장 작은 인덱스를 j로 설정한다.
                min_index = j
        # 내부 반복문을 빠져나왔다면 가장 작은 값의 인덱스가
        # min_index에 저장되어 있을 것이다.
        # i번째에 가장 작은 값이 들어가야 하므로
        # i번째 요소의 값과 min_index의 값을 맞바꾼다.(교환)
        if i == min_index: continue # 가장 작은 값이 i번째라면
        datas[i], datas[min_index] = datas[min_index], datas[i]
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
    selection_sort(datas, True)

    # 정렬 결과 출력
    print(f"정렬완료\n{datas}")