# 내 풀이
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    
    while q:
        if len(q) >= 2 and q[-1] + q[0] <= limit:
            answer += 1
            q.pop()
            q.popleft()
        else:
            q.pop()
            answer += 1
    
    return answer

# 다른 사람 풀이
def solution2(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution2([30, 30, 50, 70, 90, 100], 100))