import sys

input = sys.stdin.readline

N = int(input())
a = list(set(int(input()) for _ in range(N)))
a.sort()
for i in range(len(a)):
    print(a[i])