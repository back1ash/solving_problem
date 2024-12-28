import sys

input = sys.stdin.readline
N = int(input())
a = [input().rsplit() for _ in range(N)]

a.sort(key=lambda x : int(x[0]))
for age, name in a:
    print(f"{age} {name}")
