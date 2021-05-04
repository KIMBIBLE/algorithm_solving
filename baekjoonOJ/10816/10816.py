"""
최대 50만개의 숫자카드(N)에서 최대 50만개의 수(M)를 대상으로 몇개의 각 카드가 몇개 있는지 검사

1개의 숫자카드에 대해 검사하는 경우 O(N)의 시간이 소요되고, 
N개의 카드들을 대상으로 모두 검사하면 O(N * M)이 됨.
하지만 시간제한이 1초라 브포 방식으로는 못품

따라서 1개의 숫자 카드에 대해 검사하는 로직의 시간복잡도를 낮출 방법이 필요
O(lgN): 이진탐색 활용
O(1): 배열 활용
"""

class CardMap:
    MAX_NUM = 10000000
    MIN_NUM = -10000000

    def __init__(self):
        self.negative = [0 for _ in range(abs(CardMap.MIN_NUM) + 1)]
        self.zero = 0
        self.positive = [0 for _ in range(CardMap.MAX_NUM + 1)]

    def count(self, num):
        if num == 0:
            return self.zero
            
        elif num < 0:
            return self.negative[abs(num)]
            
        else:
            return self.positive[num]

    def mark(self, num):
        if num == 0:
            self.zero += 1
            
        elif num < 0:
            self.negative[abs(num)] += 1
            
        else:
            self.positive[num] += 1



import sys
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    N = int(readline())
    cards = list(map(int, readline().split()))
    cm = CardMap()

    for card in cards:
        cm.mark(card)

    M = int(readline())
    target = list(map(int, readline().split()))
    for t in target:
        print(cm.count(t), end=' ')
