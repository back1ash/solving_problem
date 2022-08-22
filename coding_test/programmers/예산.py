def solution(d, budget):
    answer = 0
    d.sort()
    
    for department in d:
        if budget < department:
            break
        budget -= department
        answer += 1
    return answer
