# 모든 순열을 찾아서 해결하는 방법. 시간 복잡도면에서 효율이 너무 떨어진다.
#import itertools
#def solution(numbers):
#    answer = 0
#    permutations = list(itertools.permutations(numbers, len(numbers)))
#    for permutation in permutations:
#        tmp = int("".join(map(str, permutation)))
#        answer = tmp if tmp > answer else answer
#    return str(answer)


# str sort 이용해서 풀이.
import itertools
def solution(numbers):
    answer = 0
    numbers.sort(key = lambda x:str(x)*3, reverse = True)
    answer = int("".join(map(str, numbers)))
    return str(answer)
