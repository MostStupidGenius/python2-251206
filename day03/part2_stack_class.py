# part2_stack_class.py
# 스택 자료구조
# 스택 자료구조는 나중에 들어온 데이터가(LI) 먼저 나가는(FO) 자료구조를 가리킨다.
# .append()를 통해 데이터를 추가하고 .pop()을 통해 데이터를 추출한다.

class Stack():
    def __init__(self, data:int=None):
        self.datas = [] if data is None else [data]
    
    # 큐의 요소 개수 반환
    def get_length(self):
        return len(self.datas)

    # 데이터 추가(append)
    def append(self, data:int):
        self.datas.append(data)
        return self # 체이닝 기법

    # 데이터 추출(pop())
    def get(self):
        if self.get_length() < 1: return None
        return self.datas.pop()

    # 문자열 표현
    def __str__(self) -> str:
        return f"Stack {self.datas}"

if __name__ == "__main__":
    stack = Stack() # 객체 인스턴스 생성

    # 체이닝 기법을 이용한 데이터 연속삽입
    stack\
        .append(3)\
        .append(4)\
        .append(5)
    
    print(stack) # 현재 저장된 데이터 출력
    # 저장되는 순서는 Queue 자료구조나 Stack 자료구조나 동일하다

    # 데이터 추출
    got_data = stack.get()
    # 추출된 데이터와 남은 데이터 출력
    print(f"data: {got_data}\ndatas: {stack}")