# part3_DFS_search_algorithm.py
# 깊이우선탐색
# 깊이우선탐색은 탐색 알고리즘 중 하나로, 더이상 나아갈 곳이 없을 때까지 탐색한 후
# 가장 가까운 갈림길로 돌아가서 방문하지 않은 다른 노드를 탐색하는 알고리즘이다.
# graph 데이터를 기반으로 탐색을 진행하며, 시작지점 선택,
# 각 정점(노드) 방문 여부를 저장할 visited(set자료구조) 변수가 필요하다.

# 이러한 DFS는 재귀함수 혹은 스택자료구조를 활용하여 구현할 수 있다.
# 1. 스택 자료구조 활용
def DFS_stack(graph:dict[str:list[str]], start:str, show:bool=False):
    """
    :param graph: 인접 리스트 방식으로 작성된 그래프 데이터. 정점은 모두 문자열이다.
    :type graph: dict[str: list[str]]
    :param start: 그래프에서 시작지점이 될 정점 문자열.
    :type start: str
    :param show: 중간 과정 출력 여부
    :type show: bool
    """
    # 방문여부를 저장할 set 자료구조 변수
    visited = set()
    # 시작 정점(노드)를 스택으로 사용할 리스트에 추가
    stack = [start]
    # while문을 사용하여 stack 데이터가 빌 때까지
    # ※ while문의 조건식으로 이터러블 객체를 넣으면
    # 해당 이터러블의 원소가 하나라도 있으면 True, 없으면 False를 반환한다.
    while stack: # :stack이 비어있지 않다면
        # 스택에서 정점을 꺼낸다.(가장 최근에 추가된 정점)
        vertex = stack.pop()

        # 꺼낸 정점이 아직 방문한 적이 없다면
        if vertex not in visited: # :만약에 vertex가 visited에 포함되어 있지 않다면
            # 방문처리, visited에 추가
            visited.add(vertex)
            if show: print(vertex, end=" ") # 정점 출력

            # 현재 정점(vertex)의 이웃 정점들을 스택에 추가
            # ※ if문을 활용하여 방문하지 않은 이웃 정점만 추가한다.
            # 방문하지 않은 이웃
            not_visited = [e for e in graph[vertex] if e not in visited]

            # not_visited가 비어있으면 다음 반복으로 이동
            if not not_visited: continue

            # stack 변수에 extend()를 사용하여 방문하지 않은 이웃 정점을 추가
            stack.extend(not_visited)
        # 방문한 적이 있다면 아무것도 하지 않고 다음 반복으로 이동한다.

# 2. 재귀함수를 이용한 깊이우선탐색 구현하기
def DFS_recursive(graph:dict, start:int, visited=None):
    # visited 변수가 None이면 최초호출이므로, 새로운 set을 생성한다
    # if visited is None: visited = set()
    # 한줄 코드
    visited = visited or set()

    # 현재 노드를 방문 처리
    visited.add(start)
    # 방문한 노드를 출력
    print(start, end=' ')

    # 현재 노드의 이웃 노드들을 탐색하고 재귀적으로 DFS 수행
    neightbor_nodes:list = graph[start]
    # 마지막 이웃부터 접근하려는 경우, 리스트를 반전시키고 진행해주어야 한다.
    # for문은 0번째 요소부터 접근하기 때문.
    neightbor_nodes.reverse()
    for next_node in neightbor_nodes:
        # visited에 포함되었는지 여부를 통해서
        # 방문하지 않은 노드들에 대해 재귀적으로 DFS 수행
        if next_node not in visited:
            DFS_recursive(graph, next_node, visited)

if __name__ == "__main__":
    # 인접 리스트를 이용한 그래프 표현
    graph = {
        'A': ['B', 'C'],      # A는 B, C와 연결됨
        'B': ['A', 'D', 'E'], # B는 A, D, E와 연결됨
        'C': ['A', 'F'],      # C는 A, F와 연결됨
        'D': ['B'],           # D는 B와 연결됨
        'E': ['B', 'F'],      # E는 B, F와 연결됨
        'F': ['C', 'E']       # F는 C, E와 연결됨
    }
    # DFS stack 자료구조 활용 함수 사용해보기
    # 이때, start 정점을 바꿔서 결과 예상해보기
    # A -> C -> F -> E -> B -> D
    DFS_stack(graph, start="A", show=True)
    print()
    # F -> E -> B -> D -> A -> C
    DFS_stack(graph, start="F", show=True)
    print()
    print("=" * 20)
    DFS_recursive(graph, start="F")