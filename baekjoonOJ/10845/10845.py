import sys
readline = lambda: sys.stdin.readline().rstrip()

from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
        self.__size = 0


    def empty(self):
        if self.__size == 0:
            return 1
        
        else:
            return 0

    
    def push(self, num):
        self.q.append(num)
        self.__size += 1

    
    def pop(self):
        if self.empty():
            return -1
        
        else:
            item = self.q.popleft()
            self.__size -= 1
            return item


    def size(self):
        return self.__size


    def front(self):
        if self.__size == 0:
            return -1

        else:
            return self.q[0]


    def back(self):
        if self.__size == 0:
            return -1

        else:
            return self.q[self.__size - 1]



if __name__ == '__main__':
    N = int(readline())
    q = Queue()

    for _ in range(N):
        cmd = readline()
        if cmd[:4] == 'push':
            cmd, operand = cmd.split()
            operand = int(operand)
            func = getattr(q, 'push')
            func(operand)
        
        else:
            func = getattr(q, cmd)
            print(func())
