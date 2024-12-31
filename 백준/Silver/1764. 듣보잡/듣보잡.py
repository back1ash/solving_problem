import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ear = set(input().rstrip() for _ in range(N))
see = set(input().rstrip() for _ in range(M))

earsee = sorted(list(ear.intersection(see)))
print(len(earsee))
for x in earsee:
    print(x)