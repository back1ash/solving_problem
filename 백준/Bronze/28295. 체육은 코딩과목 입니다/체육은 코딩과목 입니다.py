direction = 0
for _ in range (10):
    tmp = input()
    if tmp == "1":
        direction += 1
    if tmp == "2":
        direction += 2
    if tmp == "3":
        direction -= 1

direction = direction % 4

if direction == 0:
    print("N")
elif direction == 1:
    print("E")
elif direction == 2:
    print("S")
elif direction == 3:
    print("W")