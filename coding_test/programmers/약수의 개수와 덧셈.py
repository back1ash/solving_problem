# 약수를 모든 i보다 작은 모든 수를 대입하여 효율성이 떨어진다.
# def solution(left, right):
#     answer = 0
    
#     for i in range(left, right+1):
#         divisor = set()
#         for j in range(1,i+1):
#             if i % j == 0:
#                 divisor = divisor | set([i, j])
#         if len(divisor) % 2 == 0:
#             answer += i
#         else:
#             answer -= i
            
#     return answer

# 약수를 구하는 알고리즘에선 구하는 수의 제곱근까지만 구해도 된다.
# 이 편이 효율성을 훨씬 증대시킨다.
def solution(left, right): 
    answer = 0
    
    for i in range(left, right+1):
        divisor = set()
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                divisor = divisor | set([j, i//j])
        if len(divisor) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
            
