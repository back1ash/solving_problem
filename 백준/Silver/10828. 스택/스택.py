import sys

input = sys.stdin.readline

class Stack:
    stack = []
    def push(self, a):
        self.stack.append(a)

    def top(self):
        if len(self.stack):
            print(self.stack[-1])
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def pop(self):
        if len(self.stack):
            print(self.stack.pop())
        else:
            print(-1)

    def empty(self):
        print("0" if self.stack else "1")


N = int(input())
stack = Stack()

for _ in range(N):
    command = list(input().rstrip().split())
    if command[0] == "push":
        stack.push(command[1])
    elif command[0] == "top":
        stack.top()
    elif command[0] == "size":
        stack.size()
    elif command[0] == "empty":
        stack.empty()
    elif command[0] == "pop":
        stack.pop()