from collections import deque
def solution(priorities, location):
    answer = 0
    a = [1 if x==location else 0 for x in range(len(priorities))]
    priorities = deque(priorities)
    a = deque(a)
    
    while priorities:
        j = priorities.popleft()
        chk = a.popleft()
        if len(priorities) > 1 and max(priorities) > j:
            priorities.append(j)
            a.append(chk)
        else:
            if chk == 1:
                answer += 1
                break
            answer += 1
    return answer
