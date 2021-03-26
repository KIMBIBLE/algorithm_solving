def solution(n, lost, reserve):
    answer = 0
    state = [1 for i in range(n+2)]
    
    INVALID = -1
    state[0] = state[n+1] = INVALID
    for r in reserve:
        state[r] += 1
    
    for l in lost:
        state[l] -= 1

    for idx in range(1, n + 1):
        if state[idx] == 0:
            # check left
            if state[idx - 1] == 2:
                state[idx - 1] -= 1
                state[idx] += 1
                continue
            
            # check right
            if state[idx + 1] == 2:
                state[idx + 1] -= 1
                state[idx] += 1
                continue
    
    for each in state:
        if each >= 1:
            answer += 1
    
    return answer

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])