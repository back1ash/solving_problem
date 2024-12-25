import sys

input = sys.stdin.readline

T = int(input())
N = int(input())
candies = list(map(int, input().split()))
now = sum(candies)

print("Padaeng_i Happy" if now >= T else "Padaeng_i Cry")