# 다른 사람 풀이 1
def solution(numbers, target):
    answer = 0
    s = [[numbers[0], 0], [-numbers[0], 0]]
    
    while s:
        temp, idx = s.pop()
        idx += 1
        
        if idx < len(numbers):
            s.append([temp+numbers[idx], idx])
            s.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
                
    return answer

# 다른 사람 풀이 2
from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    
    while q:
        temp, idx = q.popleft()
        idx += 1
        
        if idx < len(numbers):
            q.append([temp + numbers[idx], idx])
            q.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    
    return answer

# 다른 사람 풀이 3
from itertools import product

def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))