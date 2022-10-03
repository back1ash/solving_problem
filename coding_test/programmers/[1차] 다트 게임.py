# 정규표현식을 이용한 토큰화를 사용하여 푼 풀이.
# tokens를 구할 때, for문 안에서 각각 re를 사용하는 것이 마음에 들지 않는다.
# 다른 사람의 풀이에서 다른 방식으로 푼 방식이 있는데, 연등 시간이 끝나간다.

import re

def solution(dartResult):
    answer = [0,0,0]
    tokens = re.findall("\d+[A-Z][*,#]?", dartResult)
    for idx, token in enumerate(tokens):
        score = int(re.search("\d+", token).group())
        bonus = re.search("[A-Z]", token).group()
        option = re.search("[*,#]", token)
        if bonus == "S":
            answer[idx] = score
        elif bonus == "D":
            answer[idx] = score ** 2
        elif bonus == "T":
            answer[idx] = score ** 3
        
        if option:
            if option.group() == "*":
                answer[idx] *= 2
                if idx != 0:
                    answer[idx-1] *= 2
            elif option.group() == "#":
                answer[idx] *= -1
                
    answer = list(map(int, answer))
    return sum(answer)
