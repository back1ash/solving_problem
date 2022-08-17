# pop으로 앞부터 요소를 꺼내와 해결하는 경우 효율성 테스트를 통과하지 못한다.
# 역순으로 pop해서 푸는 경우는 효율성 테스트랑 상관 없을 듯.
def solution(arr):
    cursor = 1
    forward = arr[0]
    answer = [forward]
    while cursor < len(arr):
        behind = arr[cursor]
        if forward != behind:
            answer.append(behind)
        forward = behind
        cursor += 1
    return answer
