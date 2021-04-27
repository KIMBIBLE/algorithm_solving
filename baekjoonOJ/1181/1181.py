import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n = int(readline())
    words = []
    for _ in range(n):
        words.append(readline())
    words = list(set(words))
    res = sorted(words, key = lambda x: (len(x), x))
    
    for word in res:
        print(word)