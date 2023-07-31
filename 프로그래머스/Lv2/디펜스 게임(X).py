# 다른 사람 코드
import heapq

def solution(n, k, enemy):
    priority = []
    
    if k >= len(enemy): return len(enemy)

    for i in range(len(enemy)):
        heapq.heappush(priority, enemy[i])
        
        if len(priority) > k:
            last = heapq.heappop(priority)
            
            if last > n:
                return i
            
            n -= last
            
    return len(enemy)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))