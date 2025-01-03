import sys

input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    li = input().split()
    if li[0] == "add":
        S.add(int(li[1]))
    elif li[0] == "remove":
        if int(li[1]) in S:
            S.remove(int(li[1]))
    elif li[0] == "check":
        print('1' if int(li[1]) in S else '0')
    elif li[0] == "toggle":
        if int(li[1]) in S:
            S.remove(int(li[1]))
        else:
            S.add(int(li[1]))
    elif li[0] == "all":
        S = set(x for x in range(1,21))
    elif li[0] == "empty":
        S = set()
