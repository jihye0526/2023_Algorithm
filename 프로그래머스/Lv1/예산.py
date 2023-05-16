# 내 풀이
def solution(d, budget):
    answer = 0
    cnt = 0
    
    d = sorted(d)
    
    for i in d:
        if answer + i <= budget:
            answer += i
            cnt += 1
    
    return cnt