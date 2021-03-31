def solution(n):
    conv = ['4', '1', '2']
    answer = ""
    
    while n:
        coef = n % 3
        answer += conv[coef]
        if coef == 0:
            coef = 3
        
        n = (n - coef) // 3
    
    return answer[::-1]
    
if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()

    for n in lines:
        print(solution(int(n)))