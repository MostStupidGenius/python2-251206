# part3_parent_class.py
# Queue 클래스와 Stack 클래스를 만들어봤다.
# 각 클래스의 메서드를 확인해보면 같은 이름의 비슷한 동작을 하는
# 메서드들이 많다.
# 비슷한 동작을 하는 메서드, 변수 등등을 부모 클래스로 추출하여
# 이를 상속받게 만들면, 공통 사항에 대해서 변경사항이 생겼을 때
# 일괄적으로 변경사항을 적용하기 편할 것이다.

# class Data_struct
class Data_struct():
    # Queue든 Stack이든 동일하게 내부적으로 list 자료구조를 사용한다.
    def __init__(self, data:int=None):
        self.datas = [] if data is None else [data]
    
    # 요소 개수 반환(공통 기능)
    def get_length(self):
        return len(self.datas)

    # 데이터 추가(append)(공통 기능)
    def append(self, data:int):
        self.datas.append(data)
        return self # 체이닝 기법

    # 데이터 추출(pop())
    def get(self, index:int):
        if self.get_length() < 1: return None
        return self.datas.pop(index)

    # 문자열 표현
    def __str__(self) -> str:
        return f"struct {self.datas}"