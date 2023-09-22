# 내 풀이
from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    order = deque([i for i in range(len(priorities))])
    
    while True:
        max_num, num, o = max(q), q.popleft(), order.popleft()
        if max_num == num:
            answer += 1
            if o == location:
                return answer
        else:
            q.append(num)
            order.append(o)

# 다른 사람 풀이
def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution2([1, 1, 9, 1, 1, 1], 0))