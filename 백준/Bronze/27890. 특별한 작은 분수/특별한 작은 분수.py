height, n = map(int, input().split())

now = 1
while now <= n:
    height = int(height/2) ^ 6 if height % 2 == 0 else (2*height) ^ 6
    now += 1

print(height)
