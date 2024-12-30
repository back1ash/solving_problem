import sys

input = sys.stdin.readline

class Queue:
    queue = []
    def push(self, a):
        self.queue.append(a)

    def front(self):
        if len(self.queue):
            print(self.queue[0])
        else:
            print(-1)
            
    def back(self):
        if len(self.queue):
            print(self.queue[-1])
        else:
            print(-1)

    def size(self):
        print(len(self.queue))

    def pop(self):
        if len(self.queue):
            print(self.queue.pop(0))
        else:
            print(-1)

    def empty(self):
        print("0" if self.queue else "1")


N = int(input())
queue = Queue()

for _ in range(N):
    command = list(input().rstrip().split())
    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "front":
        queue.front()
    elif command[0] == "back":
        queue.back()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "empty":
        queue.empty()
    elif command[0] == "pop":
        queue.pop()