# part1_queue_class.py
# 큐 자료구조 클래스로 만들기
# 큐 자료구조는 선입선출(FIFO)의 구조로,
# 먼저 들어온 자료가 먼저 나가는 자료구조를 가리킨다.
# 이를 클래스로 구현할 때에는 내부적으로 list를 사용한다.
# list의 데이터 추가(append)와 추출(pop) 메서드를 활용하여
# 큐 자료구조를 구현할 수 있다.
# 1. 정상적인 데이터가 들어오면 .append()를 통해서 저장한다.
# 2. 데이터를 추출하면 .pop(0)를 통해서 먼저 들어온(인덱스0)
#  데이터를 반환한다.
#   - 데이터가 없는 경우(len(datas) == 0) -> 어떻게 처리할 것인가


# 큐 클래스
class Queue():
    def __init__(self, data:int=None):
        # data 매개변수의 기본값을 None으로 설정
        # data에 인수가 전달되면 data에 저장되고
        # 전달되는 인수가 없으면 기본값인 None으로 초기화된다.

        # data가 None이 아니면 새로운 리스트의 요소로 만들고
        # data가 None이면 list()를 이용해 요소 없는 리스트를 생성한다
        self.datas = [data] if data is not None else list() 

    # 큐 길이 확인
    def get_length(self):
        return len(self.datas)

    # 데이터 삽입
    # 매개변수 data를 통해서 삽입할 값을 전달받은 뒤
    # .append(data)
    # 위 함수를 활용하여 데이터를 삽입/추가한다.
    def append(self, data:int):
        self.datas.append(data)
        # chainging 기법
        # self를 반환하는 것으로 외부에서
        # 객체에 대한 다른 동작을 이어서 수행할 수 있다.
        return self

    # 데이터 추출
    # 큐 자료구조이므로 데이터 추출은 먼저 들어온(인덱스0) 데이터를
    # 추출해 반환하면 된다.
    # self.datas.pop(0)
    def get(self, index:int=0): # 인덱스 외 다른 인수는 필요하지 않다.
        # self.datas에 남은 데이터의 개수가 1개 이상이어야 추출이 가능하다.
        # 개수를 미리 세어서 그 길이가 1 미만이면 None을 반환하도록 처리하자.
        if self.get_length() < 1: return None
        # 전달된 인덱스 인수가 실제 데이터 개수보다 크거나 같으면
        # 없는 인덱스가 되므로, None을 반환한다.
        if self.get_length() <= index: return None
        return self.datas.pop(index)

    # 큐 객체의 문자열 표현
    



if __name__ == "__main__":
    q = Queue(3)
    print(q.datas)
    # 데이터의 추가
    q.append(4)
    q.append(5)
    q.append(6)
    q.append(7)
    print(q.datas) # [3, 4, 5, 6, 7]

    # 데이터 추출 후 추출 데이터와 남은 큐의 데이터를 출력
    poped = q.get()
    print(f"poped: {poped}\ndatas: {q.datas}")
    poped = q.get()
    print(f"poped: {poped}\ndatas: {q.datas}")
    q.append(13)
    poped = q.get()
    print(f"poped: {poped}\ndatas: {q.datas}")
    poped = q.get()
    print(f"poped: {poped}\ndatas: {q.datas}")
    pass

