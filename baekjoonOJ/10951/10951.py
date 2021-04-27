import sys
read = lambda: sys.stdin.read().rstrip()

if __name__ == '__main__':
    x = read()+'\n'
    x = x.split('\n')
    for line in x:
        if line != '':
            a, b = map(int, line.split())
            print(a + b)