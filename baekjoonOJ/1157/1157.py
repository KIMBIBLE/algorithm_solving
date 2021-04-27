import sys, collections
readline = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    s = readline().upper()
    c = collections.Counter(s)
    list_mst = c.most_common()

    if len(list_mst) >= 2 and list_mst[0][1] == list_mst[1][1]:
        print("?")

    else:
        print(list_mst[0][0])