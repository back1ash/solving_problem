N = int(input())
result = 0

for i in range(N,1,-1):
  tmp = str(i)
  cur = i + sum([int(x) for x in tmp])
  result = i if cur == N else result

print(result)