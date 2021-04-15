import sys
readline = lambda: sys.stdin.readline()

class xyCoordinate:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

if __name__ == '__main__':
    n = int(readline())
    plans = readline().rstrip().split()
    c = xyCoordinate()

    for p in plans:
        if p == 'L' and c.y != 1:
            c.y -= 1

        elif p == 'R' and c.y != n:
            c.y += 1

        elif p == 'U' and c.x != 1:
            c.x -= 1 

        elif p == 'D' and c.x != n:
            c.x += 1

        else:
            pass

    print("{x} {y}".format(x=c.x, y=c.y))
    
