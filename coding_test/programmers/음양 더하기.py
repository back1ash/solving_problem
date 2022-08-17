def solution(absolutes, signs):
    for i in range(len(signs)):
        if not signs[i]:
            absolutes[i] = 0 - absolutes[i]
    answer = sum(absolutes)
    return answer
