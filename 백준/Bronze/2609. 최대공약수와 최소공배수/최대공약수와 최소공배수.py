import sys

input = sys.stdin.readline

a, b = map(int, input().split())
c = a*b

while b!=0:
    r = a % b
    a = b
    b = r
gcd = a
print(gcd)
print(int(c / gcd))