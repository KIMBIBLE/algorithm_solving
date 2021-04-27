import sys
readline = lambda: sys.stdin.readline().rstrip()

def check_asc(s):
    for idx in range(len(s) - 1):
        if s[idx] + 1 != s[idx + 1]:
            return False
    
    return True

def check_desc(s):
    for idx in range(len(s) - 1):
        if s[idx] - 1 != s[idx + 1]:
            return False

    return True


if __name__ == '__main__':
    s = list(map(int, readline().split()))
    
    if check_asc(s):
        print('ascending')
        exit()

    elif check_desc(s):
        print('descending')
        exit()
    
    else:
        print('mixed')
        
