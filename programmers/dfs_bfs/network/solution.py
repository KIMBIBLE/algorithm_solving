"""
* 새로운 네트워크의 기준 -> bfs 시, 새롭게 방문처리를 할 경우 플래그 세팅!

* 주의사항? : bfs 수행과정에서 특정 노드와 연결 노트를 체크할 때, 
i=i인 경우는 연결이 안된 것으로 처리?
하지만!! 예외 처리 안해도 어차피 특정 노드(i)에 대해 연결된 노드를 체크한다고 할 때, 
어차피 자기 자신은 이미 방문 처리 되어있기 때문에 
bfs 로직 상 중복으로 방문처리가되거나 큐에 삽입되는 일이 없어서 괜찮을 듯!
"""

def bfs(target, computers, visited):
    is_new_network = False
    if visited[target]:
        return is_new_network
    
    # 방문하지 않은 노드라면 방문처리하고, bfs 큐에 삽입
    queue = [target]
    visited[target] = True

    # 새로운 네트워크를 뜻하는 플래그 세팅
    is_new_network = True

    while queue:
        # queue pop -> current processing node
        cur_node = queue[0]
        del queue[0]

        # cur과 연결된 노드 중 방문안한 노드 탐색 후, 방문처리 & 큐 삽입
        for next_node in range(len(computers)):
            if computers[cur_node][next_node] == 1 \
                and visited[next_node] == False:

                visited[next_node] = True
                queue.append(next_node)

    return is_new_network

def solution(n, computers):
    answer = 0
    visited = [0] * n

    for target in range(n):
        if bfs(target, computers, visited):
            answer += 1

    return answer

if __name__ == '__main__':
    import sys
    readline = lambda: sys.stdin.readline()
    n = int(readline())

    computers = []
    for _ in range(n):
        computers.append(list(map(int, readline().split())))
    
    print(solution(n, computers))
