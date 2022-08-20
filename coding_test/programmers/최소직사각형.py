def solution(sizes):
    answer = 0
    sorted_size = list()
    for size in sizes:
        sorted_size.append([max(size), min(size)])
    
    x = max(sorted_size, key = lambda x:x[0])[0]
    y = max(sorted_size, key = lambda x:x[1])[1]
    answer = x*y
    return answer
