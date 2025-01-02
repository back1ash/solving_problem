N = int(input())

def factorial(a):
    if a in [0, 1]:
        return 1
    else:
        return a * factorial(a-1)

print(factorial(N))