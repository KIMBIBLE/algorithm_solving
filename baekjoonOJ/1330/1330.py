import sys
readline = lambda: sys.stdin.readline()

if __name__ == "__main__":
    a, b = map(int, readline().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")