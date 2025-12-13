# part4_queue_class_inherit.py
# part3에서 만든 부모 struct 클래스를 상속받은
# Queue 클래스를 구현해보자.
# 부모 클래스는 다른 파일에 있으므로, from과 import를 사용하여
# 클래스 정보를 가져와야 한다.
from part3_parent_class import Data_struct

class Queue(Data_struct):
    # 부모 클래스의 생성자(__init__)를 그대로 호출한다.
    # 추가적으로 작성할 내용이 있다면 정의를 해야 하지만
    # 있는 그대로 사용한다면 굳이 작성할 필요가 없다.
    # def __init__(self, data = None):
        # super().__init__(data)
    
    def get(self, index:int=0): # 기본 인덱스 값만 변경하면 된다.
        return super().get(index)
    
    def __str__(self):
        return f"Queue {self.datas}"

if __name__ == "__main__":
    q = Queue()
    print(q)