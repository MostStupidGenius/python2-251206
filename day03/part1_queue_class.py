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
    def __str__(self):
        return f"Queue {self.datas}"

def _():
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
    print("===" * 10)
    print(q)

if __name__ == "__main__":
    # while문을 무한 반복하여 프로그램을 구동할 거다.
    # 외부에서 Queue 객체를 생성한 뒤,
    # while문 내부에서 입력을 받아서 데이터를 저장, 추출 및 출력, 프로그램 종료
    
    # while문 외부에서 Queue 객체를 생성한 뒤 q 변수에 저장한다.
    q = Queue()
    # while문을 무한 반복한다(조건식을 == True)
    while 1: # 1은 True로 취급된다.
        # input_text 변수를 선언하여 그 값을 input("명령어 입력:")으로 초기화한다.
        input_text = input("명령어 입력:")
        # 만약에 입력된 값(input_text)이 "q"라면
        if input_text == "q": # 탈출 조건
            # while문을 탈출한다.
            break
        # 만약에 입력된 값이 "get" 문자열이라면
        if input_text == "get": # 데이터 추출
            # q 객체에 get 메서드를 이용하여 데이터를 추출한 뒤 data에 담아
            data = q.get()
            # data를 출력한다
            print(data)
        
        # 입력된 데이터가 a로 시작하고 중간에 공백문자가 있으면
        # 공백문자 뒤쪽을 데이터로 취급하여 데이터만 q.datas에 저장한다.
        # 만약에 입력된 값.startwith("a")라면
        if input_text.startswith("a"): # 첫글자가 a로 시작하면
            # 입력된 값.split(" ") -> 공백문자를 구분자로 하여 문자열을 쪼갠다면
            split_text = input_text.split(" ")
            data = split_text[1] # 문자열 a 이후 첫번째 공백 직후의 값을 가리킨다.
            q.append(int(data)) # 문자열을 정수로 변환한 뒤 queue 객체에 추가한다.

        # 위의 모든 작업이 끝난 뒤엔 남은 데이터를 출력한다.
        print(f"{q.datas}\n" + "="*10)
