# 다른 사람 풀이 1
from collections import deque

def solution(x, y, n):
    answer = -1
    q = deque()
    q.append((x, 0))
    visited = set()
    
    while q:
        val, cnt = q.popleft()
        
        if val == y:
            answer = cnt
            break
            
        if val*3 <= y and val*3 not in visited:
            visited.add(val*3)
            q.append((val*3, cnt+1))
        if val*2 <= y and val*2 not in visited:
            visited.add(val*2)
            q.append((val*2, cnt+1))
        if val+n <= y and val+n not in visited:
            visited.add(val+n)
            q.append((val+n, cnt+1))
        
    return answer

# 다른 사람 풀이 2
def solution2(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        answer+=1

    return -1

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution2(2, 5, 4))