from heapq import heappop, heappush, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first+(second*2))
        answer += 1
        
    if scoville[0] < K:
        return -1
    
    return answer
