def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt = j - i
                break
        answer.append(cnt)
    answer.append(0)
    print(answer)
    return answer

#solution([1,2,3,2,3])
solution([1,2,3,2,3,1])