def solution(lottos, win_nums):
    num_0 = lottos.count(0)
    intersection = set(lottos) & set(win_nums)
    
    best = 7 - len(intersection) - num_0
    worst = 7 - len(intersection)
    
    best = 6 if best == 7 else best
    worst = 6 if worst == 7 else worst
    
    answer = [best, worst]
    return answer
