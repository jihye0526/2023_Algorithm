# 내 풀이
def solution(n):
    answer = -1
    
    for i in range(1, int(n**0.5)+1):
        if i*i == n:
            answer = (i+1)**2
            
    return answer

print(solution(121))
print(solution(3))