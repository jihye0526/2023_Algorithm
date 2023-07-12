# 내 풀이
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        num1 = i
        num2 = 0
        while num2 < n:
            num2 += num1
            num1 += 1
        
        if num2 == n:
            answer += 1
            
    return answer

# 다른 사람 풀이
def solution2(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

print(solution(15))