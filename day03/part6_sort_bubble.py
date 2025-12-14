# part6_sort_bubble.py
# 정렬 알고리즘
# 정렬 알고리즘이란, 여러 데이터들에 대해서 정해진 순서에 따라 정렬하고 배치하는 것을
# "어떻게" 구현할 것인가를 개념적으로, 논리적으로 만들어둔 것이다.

# 기초 정렬 알고리즘 중 버블 정렬은
# 단순히 인접한 요소(원소)끼리 그 크기를 비교하여 순서를 바꾸는 것으로
# 정렬이 이루어진다.
# 버블 정렬이 끝나는 시점은 더이상 순서를 바꾸는 일이 없어질 때까지이다.
# 인접한 요소만 비교하면 되기 때문에 구현은 매우 쉽고 빠르다.
# 하지만 모든 인접한 요소를 비교해야 하기 때문에
# 이미 정렬된 부분에 대해서도 비교를 하게 된다 -> 시행 횟수 증가
# 기초 정렬 알고리즘 중에서도 가장 비효율적이다.
# 대부분의 기초 정렬 알고리즘은 O(n^2)의 시간 복잡도를 가지며
# 이는, 데이터의 양이 특정 값을 넘어가는 순간
# 기하급수적으로 시행횟수가 증가해버린다.

# 함수로 버블 정렬을 구현해보자.
def bubble_sort(datas:list, show:bool):
    # 1. 전달된 데이터를 반복문(for)으로 반복한다.
    for i in range(len(datas)):
        # 외부 반복은 path를 관장하며, 전체 데이터를 훑는 목적으로 사용된다.
        # 내부 반복은 실제로 인접한 요소끼리 비교하여 교환하는 동작을 취한다.
        for j, e in enumerate(datas): # 인덱스가 필요하기 때문에
            # enumerate()를 사용한다.
            # 만약에 i+1이 len(datas)보다 작다면
            if j+1 < len(datas):
                # 마지막 요소가 아니므로 비교를 시행한다.
                if datas[j] > datas[j+1]:
                    # 맞바꾼다.(swap)
                    datas[j], datas[j+1] = datas[j+1], datas[j]
                else:
                    # 정상적인 순서이므로 행동없이 지나간다.
                    continue
    return datas


# 테스트 환경
if __name__ == "__main__":
    # datas = [3, 1, 2, 4]
    # 데이터를 랜덤하게 섞는 방법
    import random as r
    datas = list(range(100))
    # 섞기 전 데이터 출력
    print(datas)
    r.shuffle(datas)
    # 섞은 후 데이터 출력
    print(f"셔플 후:\n{datas}")
    input("Enter 입력")
    bubble_sort(datas)
    print(datas)