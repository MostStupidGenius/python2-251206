# part1_BFS_search.py
# 너비우선탐색(BFS) Breadth First Search
# 시작노드로부터 가까운 노드를 먼저 탐색하며
# 점점 범위를 넓혀나가는 방식의 탐색 알고리즘이다.
# 미로와 같은 환경에서 출구를 찾고 할 때보다는 미로의 지도를 그리는 목적으로
# 사용될 수 있다.
# 이러한 너비우선탐색은 Queue 자료구조를 활용하여 구현할 수 있다.

# queue 자료구조를 활용하여 BFS 구현하기
def BFS_queue(graph:dict, start:str, show=False):
    # 탐색 알고리즘은 기본적으로 방문 여부를 체크하여 미방문 노드를 방문해야 하기 때문에
    # visited 변수가 반드시 필요하다
    visited = set() # 빈 셋을 생성

    # 시작노드를 Queue 자료구조에 먼저 담고 진행한다.
    queue = [start]
    # 시작노드를 방문 처리
    visited.add(start)

    # 큐가 빌 때까지 반복 수행
    while queue: # 요소가 하나라도 남아있다면 True로 취급된다.
        if show: print(queue)
        # 요소가 없으면 False로 취급되어 while문이 종료된다.
        # 큐에서 가장 왼쪽 노드(가장 먼저 들어온 노드)를 꺼낸다.
        vertex = queue.pop(0) # .pop(0)를 해야 queue에서 요소가 제거된다.
        # 현재 방문중인 정점을 출력
        print(vertex, end=" ") # 공백으로 정점 출력 구분

        # 현재 정점의 이웃정점들을 순회
        for neighbor in graph[vertex]:
            # 아직 방문하지 않은 이웃 정점에 대해서
            if neighbor not in visited:
                # 방문처리
                visited.add(neighbor)
                # Queue의 오른쪽에 이웃 정점 추가
                queue.append(neighbor)

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
    BFS_queue(graph, "A")