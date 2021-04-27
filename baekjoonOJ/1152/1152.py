import sys
readline = lambda: sys.stdin.readline().strip()

if __name__ == "__main__":
    s = readline()
    count = 0

    if s == '':
        pass
        
    else:
        for ch in s + ' ':
            if ch == ' ':
                count += 1

    print(count)
    