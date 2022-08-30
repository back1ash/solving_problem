# 리스트를 사용해서 풀어냈다. 문자열을 그대로 사용하는 것보다 상황에 맞게 자료형을 바꿔 문제를 풀어나가는 것이 재밌었다.
def solution(s):
    answer = 0
    s = list(s)
    prev = ""
    tmp = []
    for idx, i in enumerate(s):
        if prev == i:
            tmp.pop()
        else:
            tmp.append(i)
        prev = tmp[-1] if tmp else ""
    answer = 0 if tmp else 1
    return answer
