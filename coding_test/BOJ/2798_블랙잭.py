N, M = map(int, input().split())
cards = list(map(int, input().split()))
maximum = 0

for e in cards:
  for i in range(N):
    for j in range(N):
      if e==cards[i] or i==j or e==cards[j]:
        continue
      current = e + cards[i] + cards[j]
      maximum = current if maximum < current <= M else maximum

print(maximum)