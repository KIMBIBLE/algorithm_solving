import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    r = 31 #26보다 큰 소수
    M = 1234567891


    L = int(readline())
    s = list(readline())
    for i in range(L):
        s[i] = ord(s[i]) - ord('a') + 1

    h = 0
    for i in range(L):
        h += s[i] * (r ** i)

    #print(h)
    H = h % M
    print(H)