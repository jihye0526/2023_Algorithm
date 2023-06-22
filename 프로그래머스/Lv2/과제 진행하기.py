# 내 풀이
from collections import deque

def solution(plans):
    answer = []
    todos = deque([])
    
    plans.sort(key=lambda x:x[1])
    
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        plan[1] = h*60 + m
        plan[2] = plan[1] + int(plan[2])
        
    prev, end = plans[0], plans[0][2]
    
    for i in range(1, len(plans)):
        if end <= plans[i][1]:
            answer.append(prev[0])
        elif end > plans[i][1]:
            todos.append(prev)
            
        prev, end = plans[i], plans[i][2] 
            
        print(todos)
            
        if i == len(plans)-1:
            answer.append(plans[i][0])
    
    return answer