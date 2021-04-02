def solution(new_id):
    answer = ''
    black_list_special_chars = "-_~!@#$%^&*()=+[{]}:?,<>/" 
    white_list_special_chars = "-_" # '.' 는 따로 처리


    next_insertion_pos = 0
    for c in new_id:
        if ('a' <= c and c <= 'z') or c in white_list_special_chars or c.isnumeric():
            answer += c
            next_insertion_pos += 1

        # stage 1
        elif 'A' <= c and c <= 'Z':
            answer += chr(ord(c) + (ord('a') - ord('A')))
            next_insertion_pos += 1
        
        # stage 2
        elif c in black_list_special_chars:
            pass
        
        # stage 3
        elif c == '.':
            if next_insertion_pos == 0:
                answer += c
                next_insertion_pos += 1

            elif answer[next_insertion_pos - 1] == '.':
                pass

            else:
                answer += c
                next_insertion_pos += 1

        else:
            raise Exception('dbg> Err in {}'.format(c))
    
    # stage 4
    answer = answer.strip('.')

    # stage 5
    if answer == '':
        answer += 'a'

    # stage 6
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')

    # stage 7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer


if __name__ == '__main__':
    import sys
    readline = sys.stdin.readline()

    new_id = readline.rstrip()
    print(solution(new_id))