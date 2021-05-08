"""
모든 인원에 대한 순열로 구하면 시간 복잡도 터질듯.
새로운 방법이 필요한데...

solution 1
dfs/bfs 탐색을 상하좌우 기준으로만 돌리면 될 듯.
dfs/bfs 탐색 수행하며 2칸 진행하면 탐색 종료


- room을 순차탐색하며 사람이 있는 곳에 대해 다음과 같이 처리.
    - 현재 좌표 기준으로, 맨해튼 거리 기준 2칸 까지 dfs/bfs 탐색
        - 못간다면 False 리턴
    
    - 해당 좌표 기준으로 탐색 끝까지 돌았다면 True 리턴
"""
from collections import deque

ROOM_SIZE = 5
MANHATTAN_LENGTH = 2
NOT_VISITED = -1

def checkOOB(row, col):
    # out of bound access check
    if row < 0 or row >= ROOM_SIZE:
        return True
        
    # out of bound access check
    if col < 0 or col >= ROOM_SIZE:
        return True

    return False


def violationCheck(room, i, j):
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    moved = [[NOT_VISITED for _ in range(ROOM_SIZE)] for _ in range(ROOM_SIZE)]
    queue = deque([])
    queue.append((i, j))
    moved[i][j] = 0
    
    while queue:
        row, col = queue.popleft()
        
        for dx, dy in movements:
            next_row = row + dy
            next_col = col + dx
            print("next_row: {}, next_col: {}".format(next_row, next_col))
            for each in moved:
                print(each)
            
            for each in room:
                print(each)
            

            if checkOOB(next_row, next_col):
                continue

            if room[next_row][next_col] == 'P' and moved[next_row][next_col] == NOT_VISITED and moved[row][col] < MANHATTAN_LENGTH:
                print("next_row: {}, next_col: {}".format(next_row, next_col))
                print("moved : " + str(moved[next_row][next_col]))
                print('--')
                
                return True

            if room[next_row][next_col] == 'O':
                if moved[next_row][next_col] == NOT_VISITED:
                    queue.append((next_row, next_col))
                    moved[next_row][next_col] = moved[row][col] + 1 # VISITED
                    if moved[i][j] == MANHATTAN_LENGTH:
                        break
                    

    return False


def checkRoom(room):
    for i in range(ROOM_SIZE):
        for j in range(ROOM_SIZE):
            if room[i][j] == 'P':
                res = violationCheck(room, i, j)

                if res:
                    return True

    return False


def solution(places):
    answer = []
    for room in places: # 5개의 방
        print('--------')
        is_violated = checkRoom(room)
        if is_violated:
            answer.append(0)
        
        else:
            answer.append(1)
        
    return answer # [1, 0, 1, 1, 1]

if __name__ == '__main__':
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
    
    print(solution(places))