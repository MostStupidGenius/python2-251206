# part6_queue_function.py
# Queue 자료구조를 함수로 구현해보기

# 데이터를 추가하는 함수
# 매개변수: 데이터 리스트, 추가할 데이터
def enqueue(datas:list, data):
    datas.append(data) # 마지막에 데이터 추가하기
    return 

# 데이터를 추출하는 함수
# 매개변수: 데이터 리스트
# 반환값: 추출한 데이터
def dequeue(datas:list):
    data = datas.pop(0) # 첫번째 요소를 추출하여 반환한다.
    return data

if __name__ == "__main__":
    datas = []
    # 데이터 추가하기
    enqueue(datas, 3)
    print(datas)
    
    enqueue(datas, 13)
    print(datas)

    enqueue(datas, 23)
    print(datas)
    
    # 데이터를 추출하기
    data = dequeue(datas) # 3
    print(datas)

    data = dequeue(datas) # 13
    print(datas)

    # 추가
    enqueue(datas, 33)
    print(datas)

    data = dequeue(datas) # 23
    print(datas)

    # 추가
    enqueue(datas, 43)
    print(datas)
