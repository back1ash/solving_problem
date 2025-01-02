import sys

input = sys.stdin.readline
sum = 0
while True:
    tmp = int(input())
    if tmp == -1: break
    sum += tmp

print(sum)