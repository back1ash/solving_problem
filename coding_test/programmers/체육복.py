def solution(n, lost, reserve):
    #테스트 케이스 중 정렬이 안되어 넘어오는 경우가 있다고 해서 두 리스트를 정렬
    #정렬이 안 되어있는 경우 중 인덱스 번호가 중요하지 않은 자료는 정렬하는 습관을 들이자.
    lost.sort()
    reserve.sort()
    
    #여벌을 가져왔으나 도난당한 학생 처리
    intersection = set(lost) & set(reserve)
    lost = [i for i in lost if i not in intersection]
    reserve = [i for i in reserve if i not in intersection]
    
    for i, receive in enumerate(lost):
        for j, give in enumerate(reserve):
            if give-receive <= 1 and give-receive >= -1:
                lost[i] = 999
                del reserve[j]
                break

    lost = [i for i in lost if i != 999]
    answer = n - len(lost)
    return answer
