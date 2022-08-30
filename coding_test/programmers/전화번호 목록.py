# 1
# 시간 복잡도가 틀릴걸 알면서도 이중 for문을 사용함.
# 정확성 테스트는 다 통과하지만 효율성이 바닥.
"""def solution(phone_book):
    answer = True
    count = 0
    
    for p in phone_book:
        for phone_number in phone_book:
            if len(p) > len(phone_number):
                continue
            if p == phone_number[:len(p)]:
                count += 1
            if count == 2:
                answer = False
                break
        count = 0
    
    return answer"""

# 2
# 파이썬의 내장함수 startswith로 1번을 구현한 내용.
# 알고리즘은 똑같은 것 같은데 효율성 테스트 1, 2번을 통과한다.
# Startswith 선언문을 찾아서 어떻게 구현되어 있는지 알아봐야겠다.
"""def solution(phone_book):
    answer = True
    
    for number in phone_book:
        tmp = phone_book.copy()
        tmp.remove(number)
        tmp = tuple(tmp)
        if number.startswith(tmp):
            answer = False
            break
    
    return answer"""

# 3
# 정렬 후 문제를 푸는 방식. 정렬의 위대함을 다시금 느끼는 풀이.....
# 문제에서 주어지는 리스트가 순서가 중요하지 않다면 꼭 먼저 정렬을 하고 생각해보자.
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    
    return answer
    
