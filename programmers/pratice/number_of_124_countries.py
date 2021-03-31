def solution(n):
    answer = ''
    
    while n:
        remainder = n % 3
        if remainder == 0:
            remainder = 3
            answer += "4"
        
        if remainder == 1:
            answer += "1"
        
        if remainder == 2:
            answer += "2"
        
        n = (n - remainder) / 3
    
    answer = answer[::-1]
    return answer

if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    for line in lines:
        res = solution(int(line[:-1]))
        print(res)
