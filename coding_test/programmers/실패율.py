# 딕셔너리를 사용해서 풀었더니 보기엔 깔끔하지만 시간이 오래 걸린다.
# def solution(N, stages):
#     answer = []
#     fail_percent = {}
    
#     remaining = len(stages)
    
#     level = 1
#     while level <= N:
#         stop = stages.count(level)
#         if remaining == 0:
#             fail_percent[level] = 0
#         else:
#             fail_percent[level] = stop/remaining
#         remaining -= stop
#         level += 1
        
#     tmp = sorted(fail_percent.items(), key = lambda x: x[1], reverse=True)
#     answer = [stage[0] for stage in tmp]
    
#     return answer


# 리스트로 풀 경우 채점시 가장 오래 걸리는 케이스가 1.3초이므로 딕셔너리 대비 약 0.4초 줄어든다.
def solution(N, stages):
    answer = []
    fail_percent = []
    
    remaining = len(stages)
    
    level = 1
    while level <= N:
        stop = stages.count(level)
        if remaining == 0:
            fail_percent.append([level, 0])
        else:
            fail_percent.append([level, stop/remaining])
        remaining -= stop
        level += 1
        
    tmp = sorted(fail_percent, key= lambda x:x[1], reverse=True)
    answer = [stage for stage, percent in tmp]
    
    return answer
