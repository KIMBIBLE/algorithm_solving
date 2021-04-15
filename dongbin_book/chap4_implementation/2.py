import sys
readline = lambda: sys.stdin.readline()

class Time:
    def __init__(self, n = None):
        if n:
            self.hour = n
            self.min = 59
            self.sec = 59

        else:
            self.hour = 0
            self.min = 0
            self.sec = 0

    def inc(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1

            if self.min == 60:
                self.min = 0
                self.hour += 1

    def cmp(self, target):
        if self.hour == target.hour and self.min == target.min and self.sec == target.sec:
            return True

        else:
            return False

    def isContain(self, num):
        if self.hour // 10 == num or self.hour % 10 == num:
            return True
        
        if self.min // 10 == num or self.min % 10 == num:
            return True
        
        if self.sec // 10 == num or self.sec % 10 == num:
            return True

        return False


if __name__ == '__main__':
    cur_time = Time()

    n = int(readline())
    target_time = Time(n)
    
    count = 0
    while cur_time.cmp(target_time) == False:
        if cur_time.isContain(3):
            count += 1

        cur_time.inc()
    
    print(count)