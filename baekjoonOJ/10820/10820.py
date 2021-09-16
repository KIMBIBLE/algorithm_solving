from collections import Counter
import sys

readline = lambda: sys.stdin.readline()

while True:
    line = readline()
    if line:
        counter = Counter(line)
        lower_cnt = 0
        upper_cnt = 0
        digit_cnt = 0
        whitespace_cnt = 0
        for item in line:
            if ord('a') <= ord(item) and ord(item) <= ord('z'):
                lower_cnt += 1
            elif ord('A') <= ord(item) and ord(item) <= ord('Z'):
                upper_cnt += 1
            elif ord('0') <= ord(item) and ord(item) <= ord('9'):
                digit_cnt += 1
            elif item.isspace():
                whitespace_cnt += 1
            else:
                print('wtf?')
        whitespace_cnt -= 1 # 개행 제거
        print(f"{lower_cnt} {upper_cnt} {digit_cnt} {whitespace_cnt}")

    else:
        break
