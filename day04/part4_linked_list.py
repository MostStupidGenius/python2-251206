# part4_linked_list.py
# 연결 리스트
# 고정길이 배열을 사용하던 C언어에서부터 시작된 자료구조로,
# 각각의 요소를 "노드(Node)"라고 부른다.
# 각 노드는 데이터를 저장하는 변수와 다음 노드를 가리키는 변수
# 두 가지를 보유한 상태에서 연결 리스트가 이 노드들을 관리하는 방식으로 동작한다.

# 이를 클래스로 표현해보자.

class Node():
    def __init__(self, data:int, next=None): # 저장하는 데이터는 정수형만
        self.data = data
        self.next = next # 다음 노드를 저장하는 변수
        # 기본값은 None으로 설정한다.
    
    def __str__(self) -> str:
        return f"Node {self.data}"

# 연결 리스트
# 연결 리스트는 시작점에 해당하는 노드를 저장하는 방식으로 시작한다.

class Linked_list():
    def __init__(self, head:Node=None):
        self.head = head

    # 새로운 노드의 삽입
    # 전달받는 데이터는 순수 데이터일 수도 있고
    # Node 객체일 수도 있다.
    def append(self, data:int|Node):
        new_node = None
        if isinstance(data, Node):
            new_node = data
        else:
            new_node = Node(data)
        # self.head가 없으면 새로운 노드를 self.head에 넣는다.
        if not self.head:
            self.head = new_node
            # self.head = data if isinstance(data, Node) else Node(data)
            return # 데이터를 삽입 완료했으므로 조기 종료 한다.
        
        # self.head가 존재한다는 의미이다.
        # .next가 None인 Node를 찾아서 순차적으로 반복해서 탐색한다.
        # 현재 노드가 계속 바뀔 것이므로
        # current_node를 선언하여 self.head부터 시작한다.
        current_node = self.head
        while current_node.next: # 현재 노드의 다음 노드가 존재하면
            # 무한 반복
            # .next가 있으므로 current_node를 .next로 교환하여
            # 다음 노드를 탐색하게 한다.
            current_node = current_node.next
        
        # while문을 탈출했다면 그것은 current_node의 next가 None이라는 의미이다.
        # 새로운 노드를 탐색결과 나온 노드의 next에 저장한다.
        current_node.next = new_node
        return # 함수 종료






    # 특정 데이터를 보유한 노드를 제거

    # 특정 데이터를 보유한 노드를 반환

    # 전체 연결 리스트를 순회하면 그 데이터들을 하나의 리스트에 담아서 반환.