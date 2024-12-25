N = int(input())

now = 0
for i in range(N):
    i = str(i)
    if i.find("50") > -1:
        now += 2
    else:
        now += 1

print(now)