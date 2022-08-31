# 1
# 풀긴 풀었는데 리스트를 두번이나 reverse하는 것이 마음에 들지 않는다.
# 문제의 난이도보다 코드가 길고 알아보기 힘든점도 마음에 들지 않는다.
# 다른 풀이 방식으로 더 짜다가 연등이 끝나서 그냥 찝찝하게 마무리...
def solution(s):
    s = s.strip("{}").split("},{")
    s.sort(key=len, reverse=True)
    answer = []
    for i in range(len(s)):
        s[i] = set(s[i].split(","))
        
    for i in range(len(s)-1):
        s[i] = list(s[i] - s[i+1])[0]
    s[-1] = list(s[-1])[0]
    answer = list(map(int, s))
    answer.reverse()
    return answer
