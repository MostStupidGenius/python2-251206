# part4_queue.py
# Queue 자료구조
# queue는 '대기열'이라는 의미로, 먼저 들어온 데이터가 먼저 나가는
# 선입선출(First In First Out)의 자료구조를 가리킨다.
# 일반적으로 작업대기열, 티케팅 대기열, 작업 순서 등에서 사용되는
# 자료구조이다.

# 리스트의 append와 pop을 이용하여 구현해보자.

if __name__ == "__main__":
    data = []
    # 모든 데이터는 마지막에 추가된다. -> .append()
    data.append(1)
    data.append(2)
    data.append(3)
    # [1, 2, 3]
    # 선입선출 구조이므로, 먼저 들어온 0번째 요소, 1이 먼저 출력되어야 한다.
    poped = data.pop(0)
    print(poped)
    print(data)

    for _ in range(len(data)):
        poped = data.pop(0)
        print(poped)
        print(data)
    
    # 대기열은 먼저 들어온 데이터(0번째)를 먼저 내보내는(pop(0)) 구조이다.
    # 때문에 순차적으로 처리해야 하는 상황에서 사용된다.