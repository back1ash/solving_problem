import sys
import math

input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))

decimal = 0
for num in nums:
    flag = True
    if num == 1:
        continue
    if num == 2:
        decimal += 1
        continue
    for i in range(2, num):
        div = num / i
        if div == int(div):
            flag = False
            break
    if flag:
        decimal += 1

print(decimal)