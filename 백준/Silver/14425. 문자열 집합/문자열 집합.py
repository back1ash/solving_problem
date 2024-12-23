import sys

input = sys.stdin.readline
n, m = map(int, input().split())

str_set = set()
result = 0
for _ in range(n):
    str_set.add(input())

for _ in range(m):
    if input() in str_set:
        result += 1

print(result)