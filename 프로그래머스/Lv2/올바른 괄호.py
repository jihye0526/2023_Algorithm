# 내 풀이
from collections import deque

def solution(s):
    q = deque()
    
    for i in s:
        if q and q[-1] == '(' and i == ')':
            q.pop()
            continue
            
        q.append(i)
    
    return False if q else True
    
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))