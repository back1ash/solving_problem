# 코드가 파이써닉하지 않은 것 같아 많이 아쉽다.
# 다른 사람들의 코드를 참고하니 for 문 안에 a, b라는 변수를 만들고
# 이를 a, b = b, a+b 로 구현하였다.
# 코딩테스트에서는 굳이 리스트로 이전 피보나치 수열을 저장할 이유가 없으므로
# 다음 문제부터 참고해보도록 해야겠다.

def solution(n):
    answer = 0
    fibo_list = [0, 1]
    for i in range(n+1):
        len_fibo = len(fibo_list)
        if len_fibo <= i:
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    answer = fibo_list[-1] % 1234567
    return answer
