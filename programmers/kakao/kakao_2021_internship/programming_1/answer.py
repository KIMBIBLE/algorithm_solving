"""
1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"


이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 
혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

- 조건 1: 1 ≤ s의 길이 ≤ 50
    - 순차 탐색이 높은 계산복잡도 없이 가능한 범위

- 조건 2: s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
    - 앞자리 0으로 인해 자리수가 바뀌는 경우는 없음

- 조건 3: return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
    -  해당 조건은 c/c++ integer range 제한 둔 조건일 듯.

# solution 1
- s 문자를 순차적으로 탐색하면서, 알파벳-숫자 매핑을 확인하며, 새로운 result string 만들어 냄.
    - 현재 문자가 숫자인 경우: 그대로 result에 추가
    - 현재 문자가 알파벳인 경우: 
        - 알파벳-숫자 매핑을 확인하고
        - 해당 숫자 result string에 추가
        - 알파벳 숫자 만큼 인덱스 증가

- 시간복잡도
    - 50개의 문자에 대해 10개의 알파벳-숫자 매핑 검사
    - 50 * 10 = 500

"""

import sys
readline = lambda: sys.stdin.readline().rstrip()

def solution(s):
    answer = ''
    m = [ 'zero', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine' ]

    for idx, c in enumerate(s):
        if c.isnumeric():
            answer += c
        
        else:
            for i, n in enumerate(m):
                # prevent out of bound access
                if idx + len(c) > 50:
                    continue
                
                if s[idx:idx+len(n)] == n:
                    answer += str(i)

    return int(answer)

if __name__ == '__main__':
    s = readline()
    print(solution(s))
