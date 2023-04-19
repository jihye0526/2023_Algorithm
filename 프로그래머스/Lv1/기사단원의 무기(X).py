def divisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            cnt += 1
            if i**2 != n:
                cnt+=1
    
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        cnt = divisor(i)
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    
    return answer

print(solution(5, 3, 2))
print(solution(10, 3, 2))