import sys
input = sys.stdin.readline

n = int(input())
li = set()
result = 0


for _ in range(n):
  tmp = input().rstrip()
  if tmp == "ENTER":
    li = set()
  else:
    if tmp in li:
      continue
    else:
      li.add(tmp)
      result += 1

print(result)