DELETED = -1

# O(N)
def isTableEnd(table, idx): 
    flag = False
    for i in range(idx, len(table)):
        if table[i] != DELETED:
            return False

    return True

def solution(n, k, cmd):
    answer = ''

    result_table = [x for x in range(n)]
    stack = []
    idx = k

    for cur_cmd in cmd:
        #print(cur_cmd)
        #print('before idx: ' + str(idx))
        if len(cur_cmd) == 1: # No Operand
            if cur_cmd == "C": # Delete
                stack.append((result_table[idx], idx))
                result_table[idx] = DELETED
                if isTableEnd(result_table, idx):
                    idx -= 1
                
                else:
                    idx += 1
                
            
            elif cur_cmd == "Z": # Revert
                val, target_idx = stack.pop()
                result_table[target_idx] = val

            else:
                print("whatttt?????")

        else: #With Operand
            cur_cmd, operand = cur_cmd.split()
            operand = int(operand)

            if cur_cmd == "D":
                #idx += operand
                
                i = 0
                while i < operand:
                    idx += 1
                    if result_table[idx] != DELETED:
                        i += 1
                
                if idx >= n:
                    idx = n - 1


            elif cur_cmd == "U":
                #idx -= operand
                
                i = 0
                while i < operand:
                    idx -= 1
                    if result_table[idx] != DELETED:
                        i += 1

                if idx <= 0:
                    idx = 0

            else:
                print("whatttt?????")
        
        #print(result_table)
        #print('after idx: ' + str(idx))


    for val in result_table:
        if val == DELETED:
            answer += 'X'
        else:
            answer += 'O'
    
    return answer

if __name__ == '__main__':

    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
    #print(solution(8, 2, ["C", "C", "C", "C", "C", "C", "C",]))