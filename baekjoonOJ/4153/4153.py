import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    while True:
        sides = list(map(int, readline().split()))
        if sides[0] == sides[1] == sides[2] == 0:
            break

        sides.sort()
        
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            print('right')
        else:
            print('wrong')