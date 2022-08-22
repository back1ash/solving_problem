def solution(numbers):
    answer = set()
    
    for _ in range(1,len(numbers)):
        crit = numbers.pop()
        result = [crit + number for number in numbers]
        answer = answer | set(result)
        
    return sorted(list(answer))
