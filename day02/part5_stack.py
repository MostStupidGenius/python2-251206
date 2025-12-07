# part5_stack.py
# stack 자료구조
# 스택 자료구조는, 나중에 들어온 데이터가 먼저 나가는 후입선출 자료구조로,
# 일반적으로 함수의 누적 호출, 재귀함수 호출, 웹페이지에서 앞으로가기/뒤로가기 등
# 위와 같은 기능들을 구현할 때 사용되는 자료구조다.
# 스택 자료구조는 파이썬의 리스트 메서드 중 append와 pop만으로 쉽게 구현이 가능하다.



if __name__ == "__main__":
    data = []
    # 데이터는 순차적으로 쌓이기 때문에 append로 데이터를 추가한다.

    [data.append(e) for e in range(10)]

    # 초기 데이터 상태 출력
    print(data) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for _ in range(len(data)):
        poped = data.pop()
        print(f"poped: {poped}")
        print(f"data: {data}")
        print("=" * 20)