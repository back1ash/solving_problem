import sys

input = sys.stdin.readline

N = int(input())
a = [[x, 0] for x in range(10001)]

for _ in range(N):
    a[int(input())][1] += 1

for x,iter in a:
    for _ in range(iter):
        print(x)