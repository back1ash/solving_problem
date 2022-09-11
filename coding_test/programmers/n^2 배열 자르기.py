# 좌표값을 구하는 문제는 divmod를 통해 해당 좌표의 몫과 나머지를 구하면 구현이 간단하다.
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        value = max(divmod(i, n))
        answer.append(value+1)
    
    return answer
