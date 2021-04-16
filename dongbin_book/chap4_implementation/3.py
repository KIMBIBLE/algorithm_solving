import sys
readline = lambda: sys.stdin.readline()

MAPSIZE = 8

def checkValidMove(x, y):
    if x >= 0 and x < MAPSIZE and y >=0 and y < MAPSIZE:
        return True
    
    else:
        return False

if __name__ == '__main__':
    X, Y = list(readline().rstrip())
    x = ord(X) - ord('a')
    y = MAPSIZE - int(Y)
    steps = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

    counter = 0
    for dx, dy in steps:
       if checkValidMove(x + dx, y + dy):
           counter +=1

    print(counter)