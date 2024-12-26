import sys

input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == "0":
        break
    print("yes" if num == num[::-1] else "no")
