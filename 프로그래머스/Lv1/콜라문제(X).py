# 다른 사람 풀이
def solution(a, b, n):
    answer = 0
    
    while n >= a:
        remainder = n % a    
        n = (n//a) * b
        answer += n
        n += remainder
    
    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))