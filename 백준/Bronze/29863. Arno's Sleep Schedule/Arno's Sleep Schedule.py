sleep = int(input())
time = [x for x in range(20,24)]
wakeup = int(input())

addi = 0
if sleep in time:
    addi = 24-sleep
    sleep = 0
print((wakeup - sleep) + addi)