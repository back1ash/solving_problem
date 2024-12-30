import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pictorial = [input().rstrip() for _ in range(N)]

for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(pictorial[int(q)-1])
    else:
        print(pictorial.index(q)+1)