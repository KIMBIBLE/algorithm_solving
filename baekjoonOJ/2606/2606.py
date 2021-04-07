class graph:
    def __init__(self):
        import sys
        readline = lambda: sys.stdin.readline()
        self.__n = int(readline())
        self.__m = int(readline())
        self.__visited = [False] * (self.__n + 1)

        self.__graph = [[] for _ in range(self.__n + 1)]
        for _ in range(self.__m):
            start, end = map(int, readline().split())
            self.__graph[start].append(end)
            self.__graph[end].append(start)

    def printGraph(self):
        print('visited : {}'.format(self.__visited))
        print('graph: {}'.format(self.__graph))

    def countVirusInfected(self):
        count = 0
        #print(self.__visited)
        for node, visited in enumerate(self.__visited):
            if visited == True and node != 1:
                count += 1

        return count

    def dfs(self, start_node = 1):
        stack = [start_node]
        
        while stack:
            cur_node = stack.pop()
            self.__visited[cur_node] = True # 스택에서 꺼낼 때 방문 처리
            #print(cur_node, end=' -> ')

            for next_node in self.__graph[cur_node]:
                if self.__visited[next_node] == False:
                    # 현재 노드에 연결된 노드가 여러 개 있는 경우, 방문 순서는 스택 삽입 순서로 결정!
                    
                    stack.append(next_node)                 


    def dfs_recursive(self, cur_node = 1):
        self.__visited[cur_node] = True
        for next_node in self.__graph[cur_node]:
            if self.__visited[next_node] == False:
                self.dfs_recursive(next_node)


if __name__ == '__main__':
    g = graph()
    #g.printGraph()
    g.dfs_recursive()
    res = g.countVirusInfected()
    print(res)