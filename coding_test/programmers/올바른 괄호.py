def solution(s):
    answer = True
    brackets = []
    for char in s:
        if char == "(":
            brackets.append("(")
        else:
            if not brackets:
                answer = False
                return answer
            brackets.pop()
    return answer if not brackets else False
