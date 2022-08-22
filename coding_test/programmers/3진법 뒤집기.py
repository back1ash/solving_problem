def solution(n):
    answer = int(reverse_ternary(n), 3)

    return answer

def reverse_ternary(n):
    result = ""
    while n:
        n, m = divmod(n, 3)
        result += str(m)
        
    return result
