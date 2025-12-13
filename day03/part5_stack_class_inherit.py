# part5_stack_class_inherit.py
# Data_struct 부모 클래스를 상속받은 Stack 클래스 구현
# Queue클래스와 구조가 유사하기 때문에 설명은 생략

from part3_parent_class import Data_struct

class Stack(Data_struct):
    def get(self, index:int=-1): # 기본 인덱스 값만 변경하면 된다.
        return super().get(index)
    
    def __str__(self):
        return f"Stack {self.datas}"

if __name__ == "__main__":
    s = Stack()
    print(s)