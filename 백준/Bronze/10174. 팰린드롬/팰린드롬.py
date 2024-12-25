N = int(input())

for _ in range(N):
    tmp = input().lower()
    print("Yes" if tmp == tmp[::-1] else "No")