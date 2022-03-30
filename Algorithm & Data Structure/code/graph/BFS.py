from collections import deque
from subway_graph import create_station_graph


def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()  # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다
    start_node.visited = True
    queue.append(start_node)

    while queue:  # 큐에 노드가 있는 동안
        current_station = queue.popleft()  # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
            if not neighbor.visited:  # 방문하지 않은 노드면
                neighbor.visited = True  # 방문 표시를 하고
                queue.append(neighbor)  # 큐에 넣는다

"""
def bfs(graph, start_node):
    queue = deque()  # 빈 큐 생성

    # 일단 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False
    
    # 시작점 노드를 방문한 표시 후, 큐에 넣는다
    start_node.visited = True
    queue.append(start_node)
    
    # 큐에 아무 노드드 없을 때까지:
    while len(queue) != 0:
        # 큐에서 가장 앞 노드를 꺼낸다
        station_node = queue.popleft()
        
        # 이 노드에 인접해 있는 노드들을 돌면서:
        for adj_node in station_node.adjacent_stations:
            # 처음 방문한 노드면
            if adj_node.visited == False:
                # 방문한 노드로 표시
                adj_node.visited = True
                # 큐에 넣는다
                queue.append(adj_node)
"""

stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)
