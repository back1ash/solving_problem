import sys
import math

input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt = 0
for size in sizes:
    tshirt += math.ceil(size/T)

div, mod = divmod(N, P)

print(tshirt)
print(F"{div} {mod}")