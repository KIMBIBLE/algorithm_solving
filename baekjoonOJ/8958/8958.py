import sys
readline = lambda: sys.stdin.readline().rstrip()

def calc_score(tc):
    sum = 0
    score = 0

    for ox in tc:
        if ox == 'O':
            score += 1
            sum += score
        
        else:
            score = 0

    return sum

if __name__ == '__main__':
    t = int(readline())
    for _ in range(t):
        tc = readline()
        print(calc_score(tc))