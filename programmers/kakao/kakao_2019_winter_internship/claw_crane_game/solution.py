def solution(board, moves):
    answer = 0
    board_len = len(board[0])
    stack = []
    
    for pos in moves:
        # print(stack)
        for i in range(board_len):
            current = board[i][pos - 1]
            if current == 0:
                continue
            
            board[i][pos - 1] = 0
            if len(stack) and current == stack[len(stack) - 1]:
                answer += 2
                # print('prev : '+ str(stack[len(stack) - 1]))
                # print('cur  : '+ str(current))
                del stack[len(stack) - 1]
                break

            else:
                stack.append(current)
                break

    return answer

if __name__ == '__main__':
    import sys
    import copy
    readline = lambda: sys.stdin.readline()
    board = []
    board.append(list(map(int, readline().split())))
    for _ in range(1, len(board[0])):
        board.append(list(map(int, readline().split())))
    
    moves = list(map(int, readline().split()))

    for each in board:
        print(each)
    print(*moves)
    
    print(solution(copy.deepcopy(board), moves))