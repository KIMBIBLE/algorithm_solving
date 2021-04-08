NOT_VISITED = -1

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dfs(squareMap, cur_node, mark_num, cnt = 0):
    squareMap[cur_node.x][cur_node.y] = mark_num
    cnt += 1

    # 현재 위치에서 연결된 노드 검색
    if squareMap[cur_node.x][cur_node.y + 1] == NOT_VISITED: # 오른족
        cnt += dfs(squareMap, Point(cur_node.x, cur_node.y + 1), mark_num)

    if squareMap[cur_node.x + 1][cur_node.y] == NOT_VISITED: # 아래
        cnt += dfs(squareMap, Point(cur_node.x + 1, cur_node.y), mark_num)
    
    if squareMap[cur_node.x][cur_node.y - 1] == NOT_VISITED: # 왼쪽
        cnt += dfs(squareMap, Point(cur_node.x, cur_node.y - 1), mark_num)
    
    if squareMap[cur_node.x - 1][cur_node.y] == NOT_VISITED: # 위
        cnt += dfs(squareMap, Point(cur_node.x - 1, cur_node.y), mark_num)

    return cnt

if __name__ == '__main__':
    import sys
    readline = lambda: sys.stdin.readline()
    n = int(readline().rstrip())

    squareMap = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(1, n + 1):
        line = list(readline().rstrip())
        for j, val in enumerate(line, 1):
            if val != '0':
                squareMap[i][j] = NOT_VISITED


    mark_num = 0
    res = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if squareMap[i][j] == NOT_VISITED:
                mark_num += 1
                cnt = dfs(squareMap, Point(i, j), mark_num)
                res.append(cnt)


    print(mark_num)
    res.sort()
    for each in res:
        print(each)