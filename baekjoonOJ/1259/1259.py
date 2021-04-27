import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    while True:
        s = readline()
        if s == '0':
            break
        
        flag = True
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                flag = False
                break
        
        if flag:
            print('yes')

        else:
            print('no')
