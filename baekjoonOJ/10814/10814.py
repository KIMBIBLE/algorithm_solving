"""
10만개 정렬 -> N^2 정렬 알고리즘 못씀 -> NlgN 정렬알고리즘 써야함

"""
import sys
readline = lambda: sys.stdin.readline().rstrip()

class Member:
    def __init__(self, idx, age, name):
        self.idx, self.age, self.name = idx, age, name

    def print(self):
        print("{age} {name}".format(age=self.age, name=self.name))


if __name__ == '__main__':
    N = int(readline())
    members = []
    for idx in range(N):
        age, name = readline().split()
        members.append(Member(idx, int(age), name))

    members.sort(key = lambda x: (x.age, x.idx))
    for member in members:
        member.print()