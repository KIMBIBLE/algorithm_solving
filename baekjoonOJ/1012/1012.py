"""
테스트케이스 갯수: T
배추 밭의 가로길이: 1 <= M <= 50
배추 밭의 세로길이: 1 <= N <= 50

배추 위치 갯수: 1 <= K <= 2500
배추 위치: X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)

배추 최대 수(노드 수): 1 <= M * N <= 2500
각 노드에 대해 연결된 간선의 최대 수: 4(상,하,좌,우)

시간 제한: 1초

이차원 배열의 모든 요소를 대상으로 연결되어 있는 그룹을 찾는 문제.
이차원 배열의 순회를 하며, 각 요소 기준으로 dfs/bfs 탐색을 수행
현재 노드의 최대 수(V: 2500), 각 노드에 대한 간선의 최대 수(E: 4) 기준으로 
dfs/bfs 탐색에 대한 시간복잡도를 대략잡아 계산해 보면,
인접 리스트: O(V+E)
인접 행렬: O(V+E) -> 현재 노드에 대해 연결된 요소에서 방문해야 할 노드를 찾을 때,
굳이 모든 정점을 대상으로 방문 여부를 체크할 필요가 없고 상하좌우 위치만 보면 됨.
O(V^2)까지 시간 복잡도가 나올 이유가 없는듯!

따라서 V의 최대 값을 기준으로 시간복잡도를 계산해보면, 시간 제한 1초에 들어오기 위해
O(V^2)까지 사용은 무난하게 가능할 듯 하고, 최적화가 잘 된다면 O(V^3)까지도 가능할 듯!

O(V^2): 1만, O(V^3): 500

메모리 제한: 512 MB
"""

VISITED = -1
PLANTED = 1
NOT_PLANTED = 0

import sys
sys.setrecursionlimit(3000)
readline = lambda: sys.stdin.readline()

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generateGraph(m, n, k):
    graph = [[NOT_PLANTED] * (m + 2) for _ in range(n + 2)]
    for _ in range(k):
        x_pos, y_pos = map(int, readline().split())
        graph[y_pos + 1][x_pos + 1] = PLANTED

    return graph

def printGraph(graph):
    for each in graph:
        print(each)

def dfs(graph, cur_node):
    graph[cur_node.y][cur_node.x] = VISITED
    #print('x: {x_pos}, y:{y_pos}'.format(x_pos=cur_node.x, y_pos=cur_node.y))
    #printGraph(graph)

    # 오른쪽
    if graph[cur_node.y][cur_node.x + 1] == PLANTED:
        dfs(graph, Point(cur_node.x + 1, cur_node.y))
    
    # 왼쪽
    if graph[cur_node.y][cur_node.x - 1] == PLANTED:
        dfs(graph, Point(cur_node.x - 1, cur_node.y))

    # 위
    if graph[cur_node.y - 1][cur_node.x] == PLANTED:
        dfs(graph, Point(cur_node.x, cur_node.y - 1))

    # 아래
    if graph[cur_node.y + 1][cur_node.x] == PLANTED:
        dfs(graph, Point(cur_node.x, cur_node.y + 1))

if __name__ == '__main__':
    t = int(readline().rstrip())
    for _ in range(t):
        m, n, k = map(int, readline().split())
        graph = generateGraph(m, n, k)
        #printGraph(graph)
        counter = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if graph[i][j] == PLANTED:
                    counter += 1
                    #print('x(j): {x_pos}, y(i):{y_pos}'.format(x_pos=j, y_pos=i))
                    dfs(graph, Point(j, i))
                #print('next')
        
        print(counter)
