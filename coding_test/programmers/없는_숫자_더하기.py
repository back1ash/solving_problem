def solution(numbers):
    numbers = set(numbers)
    ruleset = set([1,2,3,4,5,6,7,8,9])
    answer = sum(ruleset - numbers)
    return answer
