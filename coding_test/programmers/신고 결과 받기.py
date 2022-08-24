from collections import defaultdict

# 시간 복잡도 개선에 애 먹은 문제. 중첩 for문을 최소화하고 리스트보단 dict를 사용하는 것이 시간 복잡도에 좋다.
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    count_dict = defaultdict(int)
    report_list = defaultdict(set)
    
    for elem in report:
        reporter, reported = elem.split()
        report_list[reporter].add(reported)
    
    for reporteds in report_list.values():
        for reported in reporteds:
            count_dict[reported] += 1
    
    for idx, user in enumerate(id_list):
        for reported in report_list[user]:
            if count_dict[reported] >= k:
                answer[idx] += 1
                
    return answer
