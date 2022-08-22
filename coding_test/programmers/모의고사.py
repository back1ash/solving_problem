def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = {1:0, 2:0, 3:0}
    
    idx = 0
    while idx < len(answers):
        if a[idx % len(a)] == answers[idx]:
            score[1] += 1
        if b[idx % len(b)] == answers[idx]:
            score[2] += 1
        if c[idx % len(c)] == answers[idx]:
            score[3] += 1
        idx += 1
        
                
    max_score = max(score.values())
    
    for key, value in score.items():
        if value == max_score:
            answer.append(key)
    
    return answer
