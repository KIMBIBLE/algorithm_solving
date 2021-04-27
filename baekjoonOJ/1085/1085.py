import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    x, y, w, h = map(int, readline().split())
    d_up = h - y
    d_down = y - 0
    d_left = x - 0
    d_right = w - x

    print(min(d_up, d_down, d_left, d_right))
