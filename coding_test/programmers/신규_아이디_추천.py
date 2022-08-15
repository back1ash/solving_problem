#클래스로 관리했으면 더 편리하고 보기 좋았을텐데 프로그래머스에서 풀이하느라 tmp라는 변수를 이용해 과정을 풀어나갔다.
import re

def solution(new_id):
    tmp = upper_to_lower(new_id)
    tmp = eliminate_special(tmp)
    tmp = repeated_period(tmp)
    tmp = check_both_ends(tmp)
    tmp = is_empty(tmp)
    tmp = is_too_long(tmp)
    tmp = is_too_short(tmp)
    answer = tmp
    return answer

def upper_to_lower(new_id):
    return new_id.lower()

#정규 표현식으로도 사용할 수 있으나, 그냥 translate로 구현해보고 싶었다.
def eliminate_special(new_id):
    special_rule = new_id.maketrans({
        "~": "",
        "!": "",
        "@": "",
        "#": "",
        "$": "",
        '%': "",
        "^": "",
        "&": "",
        "*": "",
        "(": "",
        ")": "",
        "=": "",
        "+": "",
        "[": "",
        "{": "",
        "]": "",
        "}": "",
        ":": "",
        "?": "",
        ",": "",
        "<": "",
        ">": "",
        "/": "",
    })
    return new_id.translate(special_rule)

#re 라이브러리를 안 쓰고 해결하려 했으나 해당 부분에서 re 사용 필요.
def repeated_period(new_id):
    pattern = "\.+"
    new_id = re.sub(pattern, ".", new_id)
    return new_id

def check_both_ends(new_id):
    if new_id == "":
        return new_id
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id != "" and new_id[-1] == ".":
        new_id = new_id[:-1]
    return new_id

def is_empty(new_id):
    return "a" if new_id == "" else new_id

def is_too_long(new_id):
    value = new_id
    if len(new_id) >= 16:
        value = new_id[:15] 
    value = check_both_ends(value)
    return value

def is_too_short(new_id):
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
    
