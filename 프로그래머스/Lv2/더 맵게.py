# 내 풀이
import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    
    for s in scoville:
        heapq.heappush(hq, s)
    
    while len(hq) >= 2 and not all(i >= K for i in hq):
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        c = a + (b*2)
        heapq.heappush(hq, c)
        answer += 1
        
    return answer if all(i >= K for i in hq) else -1

# 다른 사람 풀이
def solution2(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))