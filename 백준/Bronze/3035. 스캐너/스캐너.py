R, C, ZR, ZC = map(int, input().split())

for _ in range(R):
    tmp = input()
    line = ""
    for i in tmp:
        line += i * ZC
    for _ in range(ZR):
        print(line) 