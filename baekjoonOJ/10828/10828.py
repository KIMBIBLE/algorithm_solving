import sys
readline = lambda: sys.stdin.readline().rstrip()

class Stack:
    def __init__(self):
        self.__stack = []
        self.__size = 0


    def size(self):
        return self.__size


    def empty(self):
        if self.__size == 0:
            return 1
        
        else:
            return 0


    def push(self, operand):
        self.__stack.append(operand)
        self.__size += 1


    def pop(self):
        if self.empty():
            return -1
        
        else:
            item = self.__stack.pop()
            self.__size -= 1

            return item


    def top(self):
        if self.empty():
            return -1

        else:
            return self.__stack[self.__size - 1]


if __name__ == '__main__':
    N = int(readline())
    s = Stack()

    for _ in range(N):
        cmd = readline()
        if cmd[:4] == "push":
            cmd, operand = cmd.split()
            operand = int(operand)
            func = getattr(s, cmd)
            func(operand)
        
        else:
            func = getattr(s, cmd)
            print(func())

        