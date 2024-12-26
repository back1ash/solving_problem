import sys

input = sys.stdin.readline

while True:
    tri = list(map(int, input().split()))
    c = tri.pop(tri.index(max(tri)))
    b = tri.pop()
    a = tri.pop()    
    if a == 0 and b == 0 and c == 0:
        break
    print("right" if a**2 + b**2 == c**2 else "wrong")