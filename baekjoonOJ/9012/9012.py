"""
PS(Parenthesis String): '(', ')'
VPS: Valid PS
VPS(VPS) = VPS
VPS + VPS = VPS

2 <= 괄호문자열 길이 <= 50
시간복잡도는 크게 고려할 필요 없을듯(1초)
"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    T = int(readline())

    for _ in range(T):
        s = readline()
        stack = []
        for idx, ch in enumerate(s):
            #print(stack)
            if ch == '(':
                stack.append(ch)

            elif ch == ')':
                # match 되지 않는 경우
                if len(stack) == 0:
                    stack.append(ch) # 의도적인 False State로 종료
                    break

                # match 되는 경우
                if stack[len(stack) - 1] == '(':
                    stack.pop()


            else:
                print('whattt??')
        
        #print(len(stack))
        if len(stack) != 0:
            print('NO')

        else:
            print('YES')
