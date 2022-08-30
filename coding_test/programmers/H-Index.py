# 1
# 정렬을 이용하지 않고 풀어서 코드가 직관적이긴 하나 효율성이 엉망.
"""def solution(citations):
    answer = 0
    max_value = citations[0]
    
    for i in range(max_value, -1, -1):
        tmp = [x for x in citations if x>=i]
        if len(tmp) >= i:
            answer = i
            break
            
    return answer"""

# 2
# 정렬을 이용한 풀이는 순서가 중요하지 않은 문제에서 효율성을 비약적으로 향상시켜준다.
def solution(citations):
    citations.sort(reverse = True)
    #여기서 answer = H-index
    answer = 0
    
    for i in range(len(citations)):
        if i+1 <= citations[i]:
            answer = i+1
    return answer
    
