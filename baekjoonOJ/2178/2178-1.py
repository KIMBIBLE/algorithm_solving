import sys
readline = lambda: sys.stdin.readline()

def getInput():
    n, m = map(int, readline().split())
    # arr의 0행과 0열, 그리고 n+1 행과 m+1열 : dummy
    arr = [[0]*(m + 2) for _ in range(n + 2)]

    for i in range(1, n + 1):
        line = list(readline().rstrip())
        for j in range(1, m + 1):
            arr[i][j] = int(line[j - 1])
    
    return n, m, arr

def generateGraph(n, m, arr):
    graph = [[] for _ in range((n * m + 1))]  
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] == 0:
                continue

            cur_node = m * (i - 1) + j
            if arr[i + 1][j] == 1:
                next_node = m * i + j
                graph[cur_node].append(next_node)
                graph[next_node].append(cur_node)

            if arr[i][j + 1] == 1:
                next_node = cur_node + 1
                graph[cur_node].append(next_node)
                graph[next_node].append(cur_node)

    return graph

def bfs(graph, visited, n, m, start_node = 1):
    queue = []
    queue.append(start_node)
    visited[start_node] = True
    moved = [0] * (n * m + 1)
    moved[start_node] = 0

    while queue:
        cur_node = queue[0]
        del queue[0]
        moved[cur_node] += 1

        #print('{} '.format(cur_node), end=' ')
        if cur_node == n * m:
            return moved[n * m]

        for next_node in graph[cur_node]:
            if visited[next_node] == False:
                queue.append(next_node)
                visited[next_node] = True
                moved[next_node] = moved[cur_node]

if __name__ == '__main__':
    n, m, arr = getInput()

    """
    for each in arr:
        print(each)
    """

    graph = generateGraph(n, m, arr)
    visited = [False] * (n * m + 1)
    #print(visited)
    
    """
    for idx, line in enumerate(graph):
        print("{}: {}".format(idx, line))
    """

    res = bfs(graph, visited, n, m)
    #print('res: {}'.format(res))
    print(res)

