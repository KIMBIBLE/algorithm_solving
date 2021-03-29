CONNECTED = 1


def solution(n, m, v, g):
    #print(*_dfs(v, [], g))
    print(*dfs(n, m, v, g))
    print(*bfs(n, m, v, g))

def dfs(n, m, v, g):
    visited_node = []
    stack = [v]

    while stack:
        cur = stack[len(stack) - 1] # stack top
        if cur not in visited_node:
            visited_node.append(cur)

        is_find = False
        for i in range(0, n + 1):
            if g[cur][i] == CONNECTED and i not in visited_node:
                stack.append(i)
                is_find = True
                break
        
        if is_find == False:
            _ = stack.pop()

    return visited_node

def bfs(n, m, v, g):
    visited_node = [v]
    q = [v]

    while q: # loop until visited queue is not empty
        cur = q.pop(0)

        for i in range(1, n + 1):
            if g[cur][i] == CONNECTED and i not in visited_node:
                q.append(i)
                visited_node.append(i)

    return visited_node


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    #g = [[0] * (n + 1)] * (n + 1) # shallow copy will not be work!
    #g = [[0 for _ in range(n+1)] for __ in range(n+1)]
    g = [[0]*(n + 1) for i in range(n + 1)]

    for i in range(m):
        s, e = map(int, input().split())

        g[s][e] = CONNECTED
        g[e][s] = CONNECTED
    
    solution(n, m, v, g)