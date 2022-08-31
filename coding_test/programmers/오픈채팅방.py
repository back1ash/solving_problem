# 파이썬 dictionary 기능을 이용해 쉽게 해결할 수 있었던 문제.
# record 안에 있는 기록이 Leave면 닉네임이 포함되지 않아 split으로 그냥 나누기 애매해서 if문을 적용했다.
# 매개변수에서도 optional을 적용할 수 있는 것처럼 if문으로 나누지 않아도 nickname이 optional하게 초기화 될 수 있는 방법이 있는지 모색해봐야겠다.
def solution(record):
    answer = []
    users = {}
    tmp = []
    
    for log in record:
        tmp = log.split(" ")
        if tmp[0] == "Leave":
            do, uid = log.split(" ")
        else:
            do, uid, nickname = log.split(" ")
            users[uid] = nickname
        
    
    for log in record:
        tmp = log.split(" ")
        if tmp[0] == "Enter":
            answer.append(f"{users[tmp[1]]}님이 들어왔습니다.")
        if tmp[0] == "Leave":
            answer.append(f"{users[tmp[1]]}님이 나갔습니다.")
    return answer
