VISITED = -1
CONNECTED = 1

def solution(n, m, v, g):
    dfs_res = 0
    bfs_res = 0

def dfs(n, m, v, g):
    

def bfs(n, m, v, g):
    q = []
    q.append(v) # queue initialize
    visited_node = [v]

    while len(q): # loop until visited queue is not empty
        cur = q[0]
        del q[0]

        for i in range(1, n + 1):
            if g[cur][i] == CONNECTED and i not in visited_node:
                q.append(i)
                visited_node.append(i)
                
                g[cur][i] = VISITED
                g[i][cur] = VISITED
    for l in g:
        print(l)

    return visited_node


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    #g = [[0] * (n + 1)] * (n + 1) # shallow copy will not be work!
    g = [[0 for _ in range(n+1)] for __ in range(n+1)]

    for i in range(m):
        s, e = map(int, input().split())

        g[s][e] = CONNECTED
        g[e][s] = CONNECTED
    
    bfs_res = bfs(n, m, v, g)
    print(bfs_res)