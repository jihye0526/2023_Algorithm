# 내 풀이
def solution(n):
    answer = 0
    
    for i in range(1, int(n**0.5)+1):
        if i*i == n:
            answer += i
        elif n%i == 0:
            answer += i + int(n/i)
            
    return answer

# 다른 사람 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(solution(12))
print(sumDivisor(5))