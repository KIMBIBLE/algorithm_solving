"""
정점 갯수: 1 <= N <= 1000
간선 갯수: 0 <= M <= N * (N-1) / 2 (50만 정도)
양 끝점: 1<= u, v <= N, u != v, 간선은 한 번만

시간제한: 3초 -> N이 1000이니까 O(N^3)까지 사용 가능할 듯!
연결 요소 갯수: 모든 요소 탐색하며, dfs/bfs 방문 필요

인접 리스트 구현 시 DFS/BFS: O((N + M)) <= O(N + N^2)
인접 행렬 구현 시 DFS/BFS: O((N^2)) <= O(N^2)

모든 노드에 대해 방문해야하니까 O(N^2) * O(N) = O(N^3)
"""

import sys
sys.setrecursionlimit(2000)
readline = lambda: sys.stdin.readline()

def generateGraph(n, m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def printGraph(graph):
    for idx, each in enumerate(graph):
        print('{nodeNum} : {nodes} '.format(nodeNum=idx, nodes=each))

"""
메모리: 63756 KB
시간 : 760 ms
"""
def dfs_recursive(graph, visited, cur_node):
    """
    if visited[cur_node] == False:
        print(cur_node)
    """
    visited[cur_node] = True

    for next_node in graph[cur_node]:
        if visited[next_node] == False:
            dfs_recursive(graph, visited, next_node)

"""
pypy 실행 시(python3 실행은 시간 초과)
메모리: 221616 KB
시간 : 4424 ms
"""
def dfs_iterative(graph, visited, cur_node):
    stack = [cur_node]

    while stack:
        node = stack.pop()
        """
        if visited[node] == False:
            print(node)
        """
        visited[node] = True

        for next_node in graph[node][::-1]:
            if visited[next_node] == False:
                stack.append(next_node)


if __name__ == '__main__':
    n, m = map(int, readline().split())
    graph = generateGraph(n, m)
    #printGraph(graph)

    visited = [False] * (n + 1)
    linked_component_counter = 0
    for node in range(1, n + 1):
        if visited[node] == False:
            linked_component_counter += 1
            dfs_recursive(graph, visited, node)
            #dfs_iterative(graph, visited, node)

    print(linked_component_counter)    
