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

def _():
    stack = Stack() # 객체 인스턴스 생성

    # 체이닝 기법을 이용한 데이터 연속삽입
    stack\
        .append(3)\
        .append(4)\
        .append(5)
    
    print(stack) # 현재 저장된 데이터 출력
    # 저장되는 순서는 Stack 자료구조나 Stack 자료구조나 동일하다

    # 데이터 추출
    got_data = stack.get()
    # 추출된 데이터와 남은 데이터 출력
    print(f"data: {got_data}\ndatas: {stack}")

if __name__ == "__main__":
    # while문을 무한 반복하여 프로그램을 구동할 거다.
    # 외부에서 Stack 객체를 생성한 뒤,
    # while문 내부에서 입력을 받아서 데이터를 저장, 추출 및 출력, 프로그램 종료
    
    # while문 외부에서 Stack 객체를 생성한 뒤 stack_obj 변수에 저장한다.
    stack_obj = Stack()
    # while문을 무한 반복한다(조건식을 == True)
    while 1: # 1은 True로 취급된다.
        # input_text 변수를 선언하여 그 값을 input("명령어 입력:")으로 초기화한다.
        input_text = input("명령어 입력:")
        # 만약에 입력된 값(input_text)이 "q"라면
        if input_text == "q": # 탈출 조건
            # while문을 탈출한다.
            break
        # 숫자만 입력한 경우에도 데이터가 추가될 수 있도록 수정해보자.
        # input()을 이용하여 입력된 값은 기본적으로 문자열이다.
        # 이를 int()를 이용해 정수로 바꾸는 시도를 먼저 해본다.
        # 이때 정수로 바꿀 수 없는 문자열인 경우, Error가 발생한다.
        # try-catch를 이용하여 Error가 발생하는 경우, a, get, q 등의 동작이 실행되도록 한다.

        # 입력된 값을 int()를 이용하여 먼저 정수로 변환 시도한다.
        try:
        # 형변환 시도
            data = int(input_text)
            # 형변환에서 에러가 발생하지 않았다면 이 아래의 코드를 정상적으로 실행할 것이다.
            stack_obj.append(data)
        except ValueError as e: # 숫자로 변환 불가능한 문자열이 들어온 경우의 처리
            # 만약에 입력된 값이 "g"로 시작하는 경우라면
            if input_text.startswith("g"): # 데이터 추출
                # q 객체에 get 메서드를 이용하여 데이터를 추출한 뒤 data에 담아
                # data를 출력한다
                print(stack_obj.get())
            
            # 입력된 데이터가 a로 시작하고 중간에 공백문자가 있으면
            # 공백문자 뒤쪽을 데이터로 취급하여 데이터만 stack_obj.datas에 저장한다.
            # 만약에 입력된 값.startwith("a")라면
            if input_text.startswith("a") and " " in input_text: # 첫글자가 a로 시작하면
                # 입력된 값.split(" ") -> 공백문자를 구분자로 하여 문자열을 쪼갠다면
                split_text = input_text.split(" ")
                data = split_text[1] # 문자열 a 이후 첫번째 공백 직후의 값을 가리킨다.
                stack_obj.append(int(data)) # 문자열을 정수로 변환한 뒤 Stack 객체에 추가한다.
        finally:
            # 위의 모든 작업이 끝난 뒤엔 남은 데이터를 출력한다.
            print(f"{stack_obj.datas}\n" + "="*10)
