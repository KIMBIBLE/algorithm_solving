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
            #start_time = time.time()
            dfs_recursive(graph, visited, next_node)
            #print("--- %.40f seconds ---" % (time.time() - start_time))
            

"""
1. python3
메모리: 63000 KB
시간 : 856 ms

2. pypy3
메모리: 188480 KB
시간 : 488 ms

"""
def dfs_iterative(graph, visited, cur_node):
    ''' stack = Stack()
    stack.push(cur_node) '''
    stack = [cur_node]

    ''' while stack.isEmpty() != True: '''
    while stack:
        #start_time = time.time()
        node = stack.pop()
        
        print(node)

        #print(graph[node][::-1])
        for next_node in graph[node]:
            if visited[next_node] == False:
                stack.append(next_node)
                visited[next_node] = True

        
        #print("--- %.40f seconds ---" % (time.time() - start_time))


"""
1. python3
메모리: 70948 KB
시간 : 1904 ms

2. pypy3
메모리: 233540 KB
시간 : 6788 ms

"""
class Stack:
    def __init__(self, size = 1000000):
        self.size = size
        self.stack = [None] * self.size
        self.cur = 0

    def isEmpty(self):
        if self.cur == 0:
            return True

        else:
            return False

    def isFull(self):
        if self.cur == self.size:
            return True

        else:
            return False

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')

        item = self.stack[self.cur - 1]
        self.cur -= 1
        return item

    def push(self, item):
        if self.isFull():
            raise Exception('Stack is Full')

        self.stack[self.cur] = item
        self.cur += 1

def dfs_iterative_with_custom_stack(graph, visited, cur_node):
    stack = Stack()
    stack.push(cur_node)

    while stack.isEmpty() != True:
        #start_time = time.time()
        node = stack.pop()
        
        ''' if visited[node] == False:
            print(node) '''
        
        for next_node in graph[node]:
            if visited[next_node] == False:
                stack.push(next_node)
                visited[next_node] = True


if __name__ == '__main__':
    n, m = map(int, readline().split())
    graph = generateGraph(n, m)
    #printGraph(graph)

    visited = [False] * (n + 1)
    linked_component_counter = 0
    for node in range(1, n + 1):
        if visited[node] == False:
            linked_component_counter += 1
            #start_time = time.time()
            #dfs_recursive(graph, visited, node)
            #print("--- %.40f seconds ---" % (time.time() - start_time))
            dfs_iterative(graph, visited, node)
            #dfs_iterative_with_custom_stack(graph, visited, node)
            

    print(linked_component_counter)    
