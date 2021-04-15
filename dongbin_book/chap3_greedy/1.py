import sys
readline = lambda: sys.stdin.readline()

if __name__ == '__main__':
    count = 0
    remainder = int(readline())
    for coin in [500, 100, 50, 10]:
        coef = remainder // coin
        remainder -= coef * coin
        count += coef

    print(count)